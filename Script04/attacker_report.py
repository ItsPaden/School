#!/usr/bin/env/python3

#PADEN JOHNSON 
#11/1/2021

from geoip import geolite2
from datetime import date
import sys
from collections import Counter, defaultdict
import re
import os

syslogPath = "/home/student/Documents/School/Script04/syslog.log"

ips = []

#Opening syslog file to be parsed
with open(syslogPath) as syslogFile: 
    for line in syslogFile:
      #Iterate over each line, extract ip and add to arrays for later use
      ips.append(re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)) #Regex expression to find ip
      
#process gathered ips

#Clear Console
os.system("clear")

#Begin Report - Print date and header
currentdate = date.today()
print("--------------------")
print("Attack Report : " + str(currentdate))
print("--------------------")

#Indexing through gathered ips and dates
cnt = Counter()
finaldict = defaultdict(list)

#Count number of times ip shows up
for x in ips:
    if not x: #skip over lines without ip
      continue
    else:
      cnt[x[0]] += 1

#print(cnt)
#iterate through dict, map each ip to location and add that location back to the dictionary
# Values need to be a list to store location and count to each ip 
for key in cnt:
  location = geolite2.lookup(key).country #location lookup
  templist = [cnt[key], location]
  finaldict[key] = templist

#PRINTING TABLE
print ("{:<10} {:<10} {:<10}".format('COUNT', 'IP', 'COUNTRY'))

for key, value in finaldict.items():
    count, country = value
    print ("{:<10} {:<10} {:<10}".format(count, key, country))

