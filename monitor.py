import psutil
import time
from datetime import datetime

LOG_FILE = "logs.txt"

def get_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = time.time() - psutil.boot_time()

    health_report = f"""
Time: {datetime.now()}
CPU Usage: {cpu}%
Memory Usage: {memory}%
Disk Usage: {disk}%
System Uptime: {uptime/3600:.2f} hours
{'-'*40}
"""

    print(health_report)

    with open(LOG_FILE, "a") as file:
        file.write(health_report)

    if cpu > 80:
        print("WARNING: High CPU Usage!")

    if memory > 80:
        print("WARNING: High Memory Usage!")

    if disk > 80:
        print("WARNING: High Disk Usage!")

while True:
    get_system_health()
    time.sleep(5)