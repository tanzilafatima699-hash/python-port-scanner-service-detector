
import socket
import time

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        # Create TCP socket
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.socket.settimeout(3)

        # Connect to the IP and port
        self.socket.connect((self.ip, self.port))
    def read(self, length=1024):
        return self.socket.recv(length)
    def close(self):
        self.socket.close()

def main():
    grabber = Grabber("127.0.0.1", 8000)

    try:
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: 127.0.0.1\r\n"
            "Connection: close\r\n\r\n"
        )

        grabber.socket.sendall(request.encode())

        data = grabber.read()
        print(data.decode("utf-8", errors="replace"))

    except TimeoutError:
        print("Server did not respond in time.")

    finally:
        grabber.close()


if __name__ == "__main__":
    main()


