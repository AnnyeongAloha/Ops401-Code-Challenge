# Ops401 Code Challenge Day 12
# Author: Justin "Sage" Tabios
# Made with ChatGPT

from scapy.all import *
import ipaddress

# Define a function to perform the TCP Port Range Scanner
def tcp_port_range_scanner(target_host, start_port, end_port):
    # Loop through each port and test if it is open or closed
    for port in range(start_port, end_port+1):
        # Send SYN packet to the target host and port
        response = sr1(IP(dst=target_host)/TCP(dport=port, flags="S"), timeout=1, verbose=0)

        # Check the response flags to determine the state of the port
        if response is None:
            print(f"Port {port} is filtered or silently dropped")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # Send RST packet to gracefully close the connection
            send(IP(dst=target_host)/TCP(dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed")
        else:
            print(f"Port {port} is filtered or silently dropped")

# Define a function to perform the ICMP Ping Sweep
def icmp_ping_sweep(network_address):
    # Create a list of all addresses in the given network
    network = ipaddress.IPv4Network(network_address, strict=False)
    host_list = [str(host) for host in network.hosts()]

    # Ping all addresses on the given network except for network address and broadcast address
    online_hosts = []
    for host in host_list:
        if host == str(network.network_address) or host == str(network.broadcast_address):
            continue
        response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

        # Check the response to determine if the host is up, down, or blocking ICMP traffic
        if response is None:
            print(f"Host {host} is down or unresponsive")
        elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {host} is actively blocking ICMP traffic")
        else:
            print(f"Host {host} is responding")
            online_hosts.append(host)

    # Count how many hosts are online and inform the user
    print(f"\n{len(online_hosts)} hosts are online: {', '.join(online_hosts)}")

# Prompt user for menu choice
while True:
    print("\nMenu:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = input("Enter your choice (1/2): ")

    # TCP Port Range Scanner mode
    if choice == "1":
        # Prompt user for target host and port range
        target_host = input("Enter target host IP address: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        # Call the TCP Port Range Scanner function
        tcp_port_range_scanner(target_host, start_port, end_port)
        break

    # ICMP Ping Sweep mode
    elif choice == "2":
        #
