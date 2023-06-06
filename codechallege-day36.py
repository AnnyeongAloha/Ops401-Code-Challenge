# Ops 401 Daily Code Challenge 36 
# Justin 'Sage'
# Utilized ChatGPT

import subprocess

# Prompt user for target URL or IP address
target = input("Enter the target URL or IP address: ")

# Prompt user for port number
port = input("Enter the port number: ")

# Perform banner grabbing using netcat
print("Banner grabbing using netcat:")
netcat_command = f"nc -v {target} {port}"
netcat_output = subprocess.run(netcat_command, shell=True, capture_output=True, text=True)
print(netcat_output.stdout)

# Perform banner grabbing using telnet
print("Banner grabbing using telnet:")
telnet_command = f"telnet {target} {port}"
telnet_output = subprocess.run(telnet_command, shell=True, capture_output=True, text=True)
print(telnet_output.stdout)

# Perform banner grabbing using Nmap
print("Banner grabbing using Nmap:")
nmap_command = f"nmap -p- --script=banner {target}"
nmap_output = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
print(nmap_output.stdout)
