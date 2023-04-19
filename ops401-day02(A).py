#!/usr/bin/python3

#Import Libraries 
import os, time
from datetime import datetime
#ask user for input of ip address
Target = input("Pleaser enter an IP address\n")
#set variable for timestamp
currentTime = datetime.now()
#Infinite loops to keep pinging target
while True:
    #creates function for ping and status
    def uptime(target):
        response = os.system("ping -c 1" + target)
        #Check if host is up or down
        if response ==0:
            ping_status = ("OOOOOUUIIIIIIII")
        else:
            ping_status = ("OHHH FUCK FUCK FUCK. SHIT SHIT SHIT")
        #outpuets ping status 
        return ping_status
    #assigns uptime function with IP variable to pingstatus2 variable
    ping_status_2 = uptime(target)
    #outputs pingstatus2 variable 
    print(ping_status_2)
    #prints time stamp at the end of each ping.
    print(currentTime)
    #sleeps command for 2 seconds before completing loop and running back to the top. 
    time.sleep(2)