#!/usr/bin/python3
# This is a script that establishes a ping heartbeat to a target address

# Import libraries

import os, datetime, time, smtplib
from getpass import getpass
from datetime import datetime
# Test the mail functionality
email = input("Please provide your email\n")
password = getpass("Please provide password\n")

# Defining variables

# Creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# Perform a single ping
target = input('Enter a target IP Address:\n')
ping = os.system("ping -c 1 " + target)
# Message to be sent
message = "Message_you_need_to_send"
# Starts a TLS(Transport Layer Security) 
s.starttls()
# Authentication
s.login("anonlocalscientist@gmail.com", "jmvgahbvuxivfprw")


# Sending the mail
s.sendmail("heartbeat@bot.com","anonlocalscientist@gmail.com", message)


# Terminates the session
s.quit()

currentTime = datetime.now()
#Define a function 
def check_ping(target):
    response = os.system ("ping -c 1 " + target)

    # Check if the host is up or down and print the appropriate message
    if response == 0:
        ping_status = "Network is up"
    else:
        ping_status = "Network is down"

    return ping_status    
ping_status_2 = check_ping(target)
print(ping_status_2) 
print(currentTime)
time.sleep(2)



print(ping)




#Evaluate the response as either success or failure
#Assign success or failure to a status variable
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and





