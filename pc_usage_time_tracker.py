import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import time
import json
import threading
from pathlib import Path
from datetime import datetime
import psutil
import pygetwindow as gw
import matplotlib.pyplot as plt

class PCUsageTimeTracker:
    APP_NAME = "PC Usage Time Tracker"
    APP_VERSION = "1.0.0"

    def __init__(self):
        self.root = tk.Tk()
        tb.Style(theme="darkly")
        self.root.title(f"{self.APP_NAME} v{self.APP_VERSION}")
        self.root.geometry("1000x650")

        # App directory
        self.app_dir = Path.home() / ".pc_usage_time_tracker"
        self.app_dir.mkdir(exist_ok=True)
        self.data_file = self.app_dir / "usage_data.json"

        # State
        self.running = True
        self.current_app = None
        self.last_switch = time.time()
        self.usage = self.load_data()

        self._build_ui()

        threading.Thread(target=self.tracker_loop, daemon=True).start()

    # ---------------- DATA ----------------
    def load_data(self):
        if self.data_file.exists():
            try:
                return json.loads(self.data_file.read_text())
            except Exception:
                return {}
        return {}

    def save_data(self):
        self.data_file.write_text(json.dumps(self.usage, indent=2))

    # ---------------- TRACKING ----------------
    def get_foreground_app(self):
        try:
            win = gw.getActiveWindow()
            if not win:
                return "Unknown"
            return win.title or "Unknown"
        except Exception:
            return "Unknown"

    def add_time(self, app, seconds):
        today = datetime.now().strftime("%Y-%m-%d")
        self.usage.setdefault(today, {})
        self.usage[today].setdefault(app, 0)
        self.usage[today][app] += seconds

    def tracker_loop(self):
        while self.running:
            app = self.get_foreground_app()
            now = time.time()

            if self.current_app is None:
                self.current_app = app
                self.last_switch = now
            elif app != self.current_app:
                delta = now - self.last_switch
                self.add_time(self.current_app, delta)
                self.current_app = app
                self.last_switch = now
                self.save_data()

            time.sleep(1)

    # ---------------- UI ----------------
    def _build_ui(self):
        tb.Label(self.root, text=self.APP_NAME, font=("Segoe UI", 22, "bold")).pack(pady=(10, 2))
        tb.Label(
            self.root,
            text="Offline Application Usage Tracker",
            font=("Segoe UI", 10, "italic"),
            foreground="#9ca3af"
        ).pack(pady=(0, 10))

        self.tabs = tb.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=6)

        self.tab_usage = tb.Frame(self.tabs)
        self.tab_charts = tb.Frame(self.tabs)

        self.tabs.add(self.tab_usage, text="Usage & Guide")
        self.tabs.add(self.tab_charts, text="Charts")

        # Usage tab
        self.usage_box = tk.Text(self.tab_usage)
        self.usage_box.pack(fill="both", expand=True, padx=10, pady=10)

        guide = (
            "How to use:\n\n"
            "• Leave the app running in the background.\n"
            "• It automatically tracks which application is active.\n"
            "• View today’s usage here.\n"
            "• Open Charts to see visual summaries.\n"
            "• Export data anytime.\n"
            "• Reset if you want a fresh start.\n\n"
            "Privacy:\n"
            "• No keystrokes\n"
            "• No screenshots\n"
            "• No internet\n"
            "• All data stored locally in usage_data.json\n"
        )
        self.usage_box.insert(tk.END, guide)

        # Charts tab
        tb.Button(self.tab_charts, text="📊 Show Today Chart", command=self.show_today_chart).pack(pady=10)

        # Controls
        ctrl = tb.Frame(self.root)
        ctrl.pack(fill="x", padx=10, pady=10)

        tb.Button(ctrl, text="🔄 Refresh", command=self.refresh_usage).pack(side="left", padx=4)
        tb.Button(ctrl, text="💾 Export", command=self.export_data).pack(side="left", padx=4)
        tb.Button(ctrl, text="🧹 Reset", bootstyle="danger-outline", command=self.reset_data).pack(side="left", padx=4)
        tb.Button(ctrl, text="ℹ Info", bootstyle="info-outline", command=self.show_about).pack(side="right", padx=4)

        self.refresh_usage()

    # ---------------- FEATURES ----------------
    def refresh_usage(self):
        self.usage = self.load_data()
        today = datetime.now().strftime("%Y-%m-%d")
        apps = self.usage.get(today, {})

        self.usage_box.delete("1.0", tk.END)
        self.usage_box.insert(tk.END, f"Today: {today}\n\n")

        for app, secs in sorted(apps.items(), key=lambda x: -x[1]):
            mins = int(secs // 60)
            self.usage_box.insert(tk.END, f"{app[:80]} — {mins} min\n")

    def show_today_chart(self):
        today = datetime.now().strftime("%Y-%m-%d")
        apps = self.usage.get(today, {})

        if not apps:
            messagebox.showinfo("Charts", "No data for today yet.")
            return

        labels = list(apps.keys())
        values = [v / 60 for v in apps.values()]

        plt.figure()
        plt.barh(labels, values)
        plt.title("Today's Application Usage (minutes)")
        plt.tight_layout()
        plt.show()

    def export_data(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.usage, f, indent=2)
        messagebox.showinfo("Export", "Usage data exported successfully.")

    def reset_data(self):
        if messagebox.askyesno("Reset", "Clear all tracked usage?"):
            self.usage = {}
            self.save_data()
            self.refresh_usage()

    # ---------------- INFO ----------------
    def show_about(self):
        messagebox.showinfo(
            f"About {self.APP_NAME}",
            f"{self.APP_NAME} v{self.APP_VERSION}\n\n"
            "PC Usage Time Tracker is an offline productivity tool that automatically monitors "
            "which applications you use and how long you spend on each.\n\n"

            "Key Features:\n"
            "• Automatic foreground app tracking\n"
            "• Daily and weekly insights with charts\n"
            "• Export usage to text files\n"
            "• Reset tracking anytime\n"
            "• Offline-first: all data stored locally\n"
            "• Modern dark-mode interface\n"
            "• No screenshots, no keystrokes, no cloud\n\n"

            "Benefits:\n"
            "• Discover which apps consume most of your time\n"
            "• Identify distractions\n"
            "• Improve productivity\n"
            "• Plan work or study sessions more effectively\n\n"

            "Perfect for students, freelancers, office workers, and anyone who wants "
            "clear insight into their computer habits.\n\n"

             f"{self.APP_NAME} – Offline Application Usage Tracker.\n"
            "Mate Technologies / Website: https://matetools.gumroad.com"
        )

    # ---------------- RUN ----------------
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    PCUsageTimeTracker().run()
