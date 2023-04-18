#!/usr/bin/python3
# This is a script that establishes a ping heartbeat to a target address

# Import libraries

import os, datetime, time 

# Perform a single ping
target = "8.8.8.8"
ping = os.system("ping -c 1" + target)
print(ping)
time.sleep(2)

#Transmit a single ICMP (ping) packet to specific IP every two seconds. use an infinite while loop


#Evaluate the response as either success or failure
#Assign success or failure to a status variable
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and

#Define a function 
def check_ping(target)
    response = os.system ("ping -c 1 " + target)

    # Check if the host is up or down and print the appropriate message
    if respoonse == 0:
        ping_status = "Network is active"
    else:
        ping_status = "Network is down"

return ping_status    
