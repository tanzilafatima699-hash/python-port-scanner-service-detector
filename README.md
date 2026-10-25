Python Port Scanner & Service Detector
A beginner-friendly cybersecurity project built with Python to scan TCP ports and identify running services using Nmap.

Project Overview
This tool scans a target IPv4 address for open TCP ports and uses Nmap to detect service names and, when available, software versions.
It was developed as a hands-on project to practice Python networking, socket programming, and basic network reconnaissance.

 Features
- TCP port scanning
- Multithreaded scanning using ThreadPoolExecutor
- Open port detection
- Service and version detection using Nmap
- Scan duration measurement
- Basic input validation and error handling

Technologies Used
- Python
- Socket Programming
- Nmap
- python-nmap
- ThreadPoolExecutor

 Requirements
- Python 3
- Nmap installed on your system
- Python package: python-nmap

How to Run
1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Make sure Nmap and the required Python package are installed.
4. Run the main script: python grab_scan.py
5. Enter an IPv4 address when prompted.
6. Review the open ports and detected services in the terminal.
Example: For local testing, you can enter: 127.0.0.1
The tool will scan the local computer and attempt to identify services running on detected open ports.

What I Learned
- How TCP port scanning works
- How Python sockets establish network connections
- How multithreading can help speed up scanning
- How Nmap performs service and version detection
- Why some open ports do not reveal their service or version

Future Improvements
- Improve scanning speed
- Add report export functionality
- Improve banner grabbing for supported protocols
- Develop a web-based dashboard

