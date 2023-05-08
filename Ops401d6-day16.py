# OPS401 Daily Code Challenge
# Author: Made with ChatGPT, submitted by Sage Tabios
# Date of Revision: 08 MAy 2023
# Purpose: Brute Force Attack tool that allow users to:
#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.
# AND Accepts a user input string.
# Accepts a user input word list file path.
# Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.

# Import libraries
import time

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

# Main

if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            check_password()
        elif mode == '3':
            break
        else:
            print("Invalid selection...")
