import schedule
import time
import subprocess
from datetime import datetime

def collect_and_train():
    print(f"🔄 Running scheduled task at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("🎙️ Collecting weather data...")
    subprocess.run(["python", "-m", "data.data_collector"])

    print("🤖 Training model...")
    subprocess.run(["python", "-m", "model.forecast_model"])

    print("✅ Task completed.\n")

# Run every 15 minutes (change to every(10).seconds for testing)
schedule.every(15).minutes.do(collect_and_train)

print("📅 Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(1)
