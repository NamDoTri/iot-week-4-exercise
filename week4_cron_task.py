import psutil
import argparse
from datetime import datetime
import os

file_path = './log.csv'

def write_header():
    return "time, cpu_percent, memory_used, memory_total\n"

def write_entry(time, cpu_percent, memory_used, memory_total):
    return "{},{},{},{}\n".format(time, cpu_percent, memory_used, memory_total)

def main():
    file = open(file_path, 'a')
    if os.stat(file_path).st_size == 0:
        file.write(write_header())

    for i in range (0, count):
        time = datetime.now().timestamp()
        cpu_percent = psutil.cpu_percent(interval=interval)
        memory = psutil.virtual_memory()
        file.write(write_entry(time, cpu_percent, memory.used, memory.total))

    file.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Keep alive for a period of time to collect system stats")
    ap.add_argument('-c', '--count', type=int, default=30, help="Number of entries to collect")
    ap.add_argument('-i', '--interval', type=int, default = 1, help="Number of milliseconds to collect new entries")
    args = vars(ap.parse_args())

    count = args['count']
    interval = args['interval']

    main()