
import ipaddress
import time
import nmap
from port_scanner import Scanner


def detect_services(ip, ports):
    if not ports:
        print("No open ports found.")
        return

    nm = nmap.PortScanner()
    port_range = ",".join(str(port) for port in ports)

    print("\n--- Service Detection Results ---")

    try:
        nm.scan(
            hosts=ip,
            ports=port_range,
            arguments="-sV --version-light"
        )

        if ip not in nm.all_hosts():
            print("No host results returned.")
            return

        for port, details in sorted(nm[ip]["tcp"].items()):
            print(f"\nPort: {port}")
            print(f"State: {details.get('state', 'unknown')}")
            print(f"Service: {details.get('name') or 'Unknown'}")
            print(f"Product: {details.get('product') or 'Unknown'}")
            print(f"Version: {details.get('version') or 'Unknown'}")

    except nmap.PortScannerError as error:
        print(f"Nmap error: {error}")


def main():
    ip = input("Enter target IPv4 address: ").strip()

    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        print("Invalid IPv4 address!")
        return

    scanner = Scanner(ip)
    start = time.time()

    print(f"\nScanning {ip}...")
    scanner.scan(1, 10000)

    if scanner.open_ports:
        detect_services(ip, scanner.open_ports)
    else:
        print("No open ports found.")

    print(f"\nTotal time: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    main()
