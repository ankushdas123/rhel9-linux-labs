import os
import time
# Path to your Samba share (from Windows perspective)
WATCH_DIR = r"\\192.168.1.101\ankush\Documents"
# Print messages moved to the top so you see immediate output upon running
print("=" * 60)
print(f"👀 [START] Monitoring Linux Samba Directory: {WATCH_DIR}")
print("   Waiting for new files... Press Ctrl+C to stop the automation.")
print("=" * 60)
# Take initial snapshot of the directory
try:
    before = dict([(f, None) for f in os.listdir(WATCH_DIR)])
except FileNotFoundError:
    print("❌ Error: Samba path not found! Is the Linux server running?")
    exit()
try:
    while True:
        time.sleep(2)  # Scans the Linux folder every 2 seconds
        # Take a snapshot of the current files
        after = dict([(f, None) for f in os.listdir(WATCH_DIR)])
        # Compare states to detect new files
        added = [f for f in after if not f in before]
        if added:
            for file_name in added:
                print(f"\n🔥 [ALERT] New file landed on Linux Server!")
                print(f"📂 File Name: {file_name}")
                print(f"⏰ Detected At: {time.strftime('%H:%M:%S')} | status: SUCCESS")
                print("-" * 50)
            # Update baseline to prevent duplicate alerts
            before = after
except KeyboardInterrupt:
    print("\n👋 [STOP] Automation stopped by user. Peace out!")

