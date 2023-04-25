# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Justin 'Sage Odom' Tabios
# Date of latest revision: 24 April 2023
# Purpose: Ops Challenge: File Encryption Script Part 1 of 3

# In Python, create a script that utilizes the cryptography library to:

# Prompt the user to select a mode:
# Encrypt a file (mode 1)
# Decrypt a file (mode 2)
# Encrypt a message (mode 3)
# Decrypt a message (mode 4)
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# Depending on the selection, perform one of the below functions. You’ll need to create four functions:
# Encrypt the target file if in mode 1.
# Delete the existing target file and replace it entirely with the encrypted version.
# Decrypt the target file if in mode 2.
# Delete the encrypted target file and replace it entirely with the decrypted version.
# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.
# Decrypt the string if in mode 4.
# Print the cleartext to the screen.

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet

# Declare Functions

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

# Main

# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = "hello friend".encode()
print("Plaintext is " + str(message.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)

# Encrypt the message
encrypted = f.encrypt(message)

# Print how it looks
print("Ciphertext is " + encrypted.decode('utf-8'))

# Fernet module is imported from the cryptography package
from cryptography.fernet import Fernet

# Key is generated
key = Fernet.generate_key()

# Value of key is assigned to a variable
f = Fernet(key)

# The plaintext is converted to ciphertext
token = f.encrypt(b"welcome to cybersecurity")

# Display the ciphertext
print(token)

# Decrypting the ciphertext
d = f.decrypt(token)

# Display the plaintext
print(d)
