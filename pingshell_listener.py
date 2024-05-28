import socket
import io
import time

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
