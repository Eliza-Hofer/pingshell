import subprocess
import paramiko

# Define your IP addresses and credentials
credentials = {
    "192.168.1.196": {"username": "smokey", "password": "Ee391001771"},
    "192.168.1.226": {"username": "bandit", "password": "lilith"},
    "192.168.1.222": {"username": "Eliza", "password": "Ee391001771"}
}

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
    
    if ip_address in credentials:
        username = credentials[ip_address]["username"]
        password = credentials[ip_address]["password"]
        
        ssh_client.connect(ip_address, username=username, password=password)
        ssh_client.exec_command("ping -c 1 TARGET HERE")
        ssh_client.close()
    else:
        print(f"No credentials found for IP address: {ip_address}")

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
                send_ping("192.168.1.168")
            elif char == "0":
                send_ping("192.168.1.226")
            # Handle spaces (optional)

if __name__ == "__main__":
    main()
