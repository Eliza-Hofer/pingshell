import subprocess
import paramiko

# Define your three IP addresses
IP_ADDRESS_1 = "192.168.1.1"
IP_ADDRESS_2 = "192.168.1.2"
IP_ADDRESS_3 = "192.168.1.3"

def read_binary_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            binary_str = file.read().replace(" ", "")
            return binary_str
    except FileNotFoundError:
        return None

def send_ping(ip_address):
    # Execute the ping command via SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_address, username="your_username", password="your_password")
    ssh_client.exec_command("ping -c 1 google.com")
    ssh_client.close()

def main():
    file_path = "binary_input.txt"
    binary_str = read_binary_from_file(file_path)

    if binary_str:
        for char in binary_str:
            if char == "1":
                send_ping(IP_ADDRESS_1)
            elif char == "0":
                send_ping(IP_ADDRESS_2)
            # Handle spaces (optional)

if __name__ == "__main__":
    main()