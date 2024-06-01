import subprocess
import paramiko

# Define your three IP addresses
IP_ADDRESS_1 = "192.168.1.168"
IP_ADDRESS_2 = "192.168.1.226"
IP_ADDRESS_3 = "192.168.1.222"

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
    ssh_client.exec_command("ping -c 1 TARGET HERE")
    ssh_client.close()

def string_to_binary(input_string):
    # Convert each character in the string to its binary representation
    binary_string = ' '.join(format(ord(char), '08b') for char in input_string)
    return binary_string

def write_binary_to_file(binary_string, file_path):
    # Write the binary string to a .txt file
    with open(file_path, 'w') as file:
        file.write(binary_string)

def main():
    user_input = input("Send command: ")
    
    # Convert the string to binary
    binary_string = string_to_binary(user_input)
    
    # Specify the output file path
    file_path = "binary_string.txt"
    
    # Write the binary string to the file
    write_binary_to_file(binary_string, file_path)
    
    file_path = "binary_string.txt"
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