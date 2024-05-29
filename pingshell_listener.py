import socket
import io
import time
import os
import platform
import subprocess

from crontab import CronTab

def create_cron_job(python_file_path, interval='* * * * *'):
    """
    Creates a scheduled task to execute a Python file at a specified interval.
    Works on both Linux (cron job) and Windows (Task Scheduler).

    Args:
        python_file_path (str): The path to the Python file to be executed.
        interval (str): The cron interval string for Linux. Defaults to '* * * * *' (every minute).
                        For Windows, use a format like 'hourly', 'daily', etc.
    """
    system = platform.system()
    
    if system == 'Linux':
        # Set up a cron job for Linux
        cron = CronTab(user=True)
        job = cron.new(command=f'python {python_file_path}', comment='My Python script')
        job.setall(interval)
        cron.write()
        print(f"Cron job created on Linux to run {python_file_path} at interval '{interval}'")
    
    elif system == 'Windows':
        # Set up a scheduled task for Windows using schtasks
        task_name = 'MyPythonScript'
        trigger_type = 'DAILY'  # Default to daily, can be modified
        
        # Map cron interval to schtasks trigger type (simple mapping)
        if interval == '* * * * *':
            trigger_type = 'MINUTE'
        elif interval == '0 0 * * *':
            trigger_type = 'DAILY'
        
        # Create the command for schtasks
        command = f'schtasks /create /tn {task_name} /tr "python {python_file_path}" /sc {trigger_type} /f'
        
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Scheduled task created on Windows to run {python_file_path} with trigger '{trigger_type}'")
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
