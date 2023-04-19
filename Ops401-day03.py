# Ops401 Code Challenge day 03
# Author: Justin 'Sage Odom' Tabios
# Date of revision: 19 APR 2023
# Purpose: Add on from uptime sensor tool

#!/usr/bin/python3
# This is a script that establishes a ping heartbeat to a target address

# Import libraries

import os, datetime, time, smtplib

# Defining variables
# Creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# Perform a single ping
target = "8.8.8.8"
ping = os.system("ping -c 1" + target)
# Message to be sent
message = "Message_you_need_to_send"

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

# Starts a TLS(Transport Layer Security) 
s.starttls()
# Authentication
s.login("sender_email_id", "sender_email_id_password")


# Sending the mail
s.sendmail("sender_email_id","receiver_email_id", message)


# Terminates the session
s.quit()

print(ping)




#Evaluate the response as either success or failure
#Assign success or failure to a status variable
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and



print(ping_status_2)
print(datetime.datetime.now)
time.sleep(2)

