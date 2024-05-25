import socket
import io
def main():
    addr1 = "ip address here"
    addr2 = "different ip here"
    file_path = "config.txt"


    # make nessicary files 
    with io.open(file_path, 'w', encoding='utf-8') as file:
        file.write("config placeholder")

    # Create a raw socket
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
        while True:
            packet, addr = s.recvfrom(1024)
            print(f"Received ping from {addr[0]}")
            if addr == addr1 :
                print("do stuff here")
                with open("incoming.txt", "a") as file:
                    file.write("0")
            elif addr == addr2 :
                print("other stuff here")
                with open("incoming.txt", "a") as file:
                    file.write("1")

if __name__ == "__main__":
    main()
