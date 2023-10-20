from socket import *


if __name__ == "__main__":
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(("0.0.0.0", 9999))
    print("listening on 0.0.0.0:9999")
    data = s.recvfrom(1024)
    print(data[0].decode("utf-8"))
    s.close()
