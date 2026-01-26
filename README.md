# PC Usage Time Tracker v1.0.0 – Offline Application Activity Monitor (Full Source Code)

PC Usage Time Tracker v1.0.0 is a Python desktop application for **automatically tracking how much time you spend in each active application on your computer**.  
This repository contains the full source code, allowing you to customize **tracking logic, data storage, UI layout, charts, exporting, and productivity features** for personal, professional, or learning purposes.

------------------------------------------------------------
🌟 FEATURES
------------------------------------------------------------

- 🖥️ Automatic Foreground App Tracking — Detects which window is currently active
- ⏱️ Real-Time Usage Logging — Records time spent per application continuously
- 📅 Daily Organization — Usage grouped by date automatically
- 📊 Built-In Charts — Visualize today’s application usage with bar charts
- 💾 Local JSON Storage — All data saved offline in `usage_data.json`
- 📤 Export Data — Export usage history to a text file anytime
- 🔄 Refresh View — Instantly reload today’s statistics
- 🧹 Reset Tracking — Clear all usage data for a fresh start
- 🧵 Background Threading — Tracker runs without freezing the UI
- 🎨 Modern Dark UI — Built with Tkinter + ttkbootstrap
- 📘 Built-In Guide & About — Usage instructions and feature overview included
- 🔐 Privacy First:
  - No screenshots  
  - No keystrokes  
  - No internet  
  - 100% local storage  

------------------------------------------------------------
🚀 INSTALLATION
------------------------------------------------------------

1. Clone or download this repository:

```
git clone https://github.com/rogers-cyber/PCUsageTimeTracker.git
cd PCUsageTimeTracker
```

2. Install required Python packages:

```
pip install ttkbootstrap psutil pygetwindow matplotlib
```

(Tkinter is included with standard Python installations.)

3. Run the application:

```
python PCUsageTimeTracker.py
```

4. Optional: Build a standalone executable using PyInstaller:

```
pyinstaller --onefile --windowed PCUsageTimeTracker.py
```

------------------------------------------------------------
💡 USAGE
------------------------------------------------------------

1. Start the Application:
   - Launch the program and leave it running in the background

2. Automatic Tracking:
   - The app continuously monitors which window is active
   - Time is accumulated per application automatically

3. View Today’s Usage:
   - Open the **Usage & Guide** tab to see minutes spent per app

4. Charts:
   - Go to the **Charts** tab
   - Click **📊 Show Today Chart** for a visual summary

5. Refresh:
   - Click **🔄 Refresh** to reload today’s statistics

6. Export:
   - Click **💾 Export** to save your usage data as a text file

7. Reset:
   - Click **🧹 Reset** to clear all tracked usage

8. Help / About:
   - Click **ℹ Info** for feature overview and developer information

------------------------------------------------------------
⚙️ CONFIGURATION OPTIONS
------------------------------------------------------------

Option                     Description
-------------------------- --------------------------------------------------
Automatic Tracking         Detects active foreground application every second
Usage View                 Displays today’s app usage in minutes
Charts                     Horizontal bar chart of today’s activity
Refresh                    Reload data from local storage
Export                     Save usage history to external file
Reset                      Clear all tracked data
About / Guide              Built-in help and feature overview
Local Storage              JSON-based offline storage in user home directory

------------------------------------------------------------
📦 OUTPUT
------------------------------------------------------------

- usage_data.json — Local file storing daily application usage  
- Exported TXT File — Manual export of usage history  
- Charts — On-demand matplotlib visualizations  

------------------------------------------------------------
📦 DEPENDENCIES
------------------------------------------------------------

- Python 3.10+
- ttkbootstrap — Modern themed UI
- psutil — System utilities (future expansion support)
- pygetwindow — Active window detection
- matplotlib — Usage charts
- Tkinter — Standard Python GUI framework
- pathlib, threading, json, datetime, time — Core application logic

------------------------------------------------------------
📝 NOTES
------------------------------------------------------------

- Tracking runs in a background thread to keep UI responsive
- Data is saved automatically on application switches
- Fully offline: no network connections required
- Usage is grouped per day for easy productivity review
- Portable when compiled as a standalone executable
- Ideal for productivity tracking, study monitoring, or digital wellness

------------------------------------------------------------
👤 ABOUT
------------------------------------------------------------

PC Usage Time Tracker v1.0.0 is maintained by **Mate Technologies**, delivering a **simple, privacy-friendly offline productivity tracking solution**.

Website: https://matetools.gumroad.com

------------------------------------------------------------
📜 LICENSE
------------------------------------------------------------

Distributed as commercial source code.  
You may use it for personal or commercial projects.  
Redistribution, resale, or rebranding as a competing product is not allowed.
