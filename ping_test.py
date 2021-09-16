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

gatetest = subprocess.run(["ping", "-c 3", str(default)], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if gatetest.returncode == 0:
    print("FUNCTIONAL")
elif gatetest.returncode == 1:
    print("NOT WORKING")

print()

#Ping the remote IP
print("Remote IP connection: ")

remotetest = subprocess.run(["ping", "-c 3", remote], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if remotetest.returncode == 0:
    print("FUNCTIONAL")
elif remotetest.returncode == 1:
    print("NOT WORKING")

print()

#Ping URL
print("DNS connection: ")

dnstest = subprocess.run(["ping", "-c 3", url], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if dnstest.returncode == 0:
    print("FUNCTIONAL")
elif dnstest.returncode == 1:
    print("NOT WORKING")

print()

#while loop until user enters to exit script
go = True
while(go):
    prompt = input("Press enter once you are ready to exit. ")
    if(prompt == ""):
        go = False
    