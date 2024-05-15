import socket

def main():
    addr1 = "ip address here"
    addr2 = "different ip here"
    # Create a raw socket
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
        while True:
            packet, addr = s.recvfrom(1024)
            print(f"Received ping from {addr[0]}")
            if addr == addr1 :
                print("do stuff here")
            elif addr == addr2 :
                print("other stuff here")

if __name__ == "__main__":
    main()
