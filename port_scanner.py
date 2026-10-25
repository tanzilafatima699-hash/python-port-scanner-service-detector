
import socket
import time
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f"Scanner({self.ip})"

    def add_port(self, port):
        self.open_ports.append(port)

    def is_open(self, port):
        try:
            with socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            ) as s:
                s.settimeout(0.2)
                result = s.connect_ex((self.ip, port))
                return result == 0
        except OSError:
            return False

    def scan(self, lower_port, upper_port):
        self.open_ports.clear()
        ports = range(lower_port, upper_port + 1)

        with ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(self.is_open, ports)

            for port, is_open in zip(ports, results):
                if is_open:
                    print(f"[+] Port {port} is OPEN")
                    self.add_port(port)

        print("\n--- Open Ports List ---")

        if self.open_ports:
            print(self.open_ports)
        else:
            print("No open ports found in this range.")

    def write(self, filepath, duration):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("PORT SCAN REPORT\n")
            file.write("================\n")
            file.write(f"Target IP: {self.ip}\n")
            file.write(f"Scan Date: {datetime.now()}\n")
            file.write(f"Total Open Ports: {len(self.open_ports)}\n")
            file.write(f"Scan Duration: {duration:.2f} seconds\n")
            file.write("\nOpen Ports:\n")

            if self.open_ports:
                for port in self.open_ports:
                    file.write(f"Port {port}: OPEN\n")
            else:
                file.write("No open ports found.\n")


def timefunc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
        return result

    return wrapper


@timefunc
def main():
    # Validate IP address
    while True:
        ip = input("Enter the IP address: ")

        try:
            ipaddress.IPv4Address(ip)
            break
        except ipaddress.AddressValueError:
            print("Invalid IPv4 address! Try again.")

    # Validate starting port
    while True:
        try:
            start_port = int(input("Enter the starting port: "))

            if 1 <= start_port <= 65535:
                break

            print("Port must be between 1 and 65535.")

        except ValueError:
            print("Please enter a valid number.")

    # Validate ending port
    while True:
        try:
            end_port = int(input("Enter the ending port: "))

            if not 1 <= end_port <= 65535:
                print("Port must be between 1 and 65535.")
            elif end_port < start_port:
                print("Ending port must be >= starting port.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    scanner = Scanner(ip)

    print(f"\nScanning {ip}...")
    start_time = time.time()

    scanner.scan(start_port, end_port)

    duration = time.time() - start_time

    scanner.write("open_ports.txt", duration)

    print("\nScan complete.")
    print("Open ports saved to open_ports.txt")


if __name__ == "__main__":
    main()
