#PADEN JOHNSON 
#9/12/2021

#!/usr/bin/env python

import os
import subprocess

remote = "129.21.3.17"
url = "www.google.com"

os.system("clear")

print("NETWORK CONNECTIVITY TEST")
print()
print("...I AM HERE TO HELP")
print("One moment please!")
print()

#Ping the gateway - Find gateway using system function
print("Gateway connection: ")

default = os.system("route -n | grep 'G[ \t]' | awk '{print $2}'")

gatetest = subprocess.run(["ping", default])

if gatetest == 0:
    print("FUNCTIONAL")
elif gatetest == 1:
    print("NOT WORKING")

print()

#Ping the remote IP
print("Remote IP connection: ")

remotetest = subprocess.run(["ping", remote])

if remotetest == 0:
    print("FUNCTIONAL")
elif remotetest == 1:
    print("NOT WORKING")

print()

#Ping URL
print("DNS connection: ")

dnstest = subprocess.run(["ping", url])

if dnstest == 0:
    print("FUNCTIONAL")
elif dnstest == 1:
    print("NOT WORKING")

print()

#while loop until user enters to exit script
go = True
while(go):
    prompt = input("Press enter once you are ready to exit. ")
    if(prompt == ""):
        go = False
    