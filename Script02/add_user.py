#PADEN JOHNSON 
#10/1/2021

#!/usr/bin/env python3

#Coding/Testing for script was done on a kali machine which hopefully explains further comments

import os
import subprocess
import sys
import csv

users_file = "linux_users.csv"
default_pass = "password"

fields = []
rows = []
users = []

#EmployeeID,LastName,FirstName,Office,Phone,Department,Group

def add_user(username, id, office, phone, dept, group): #user add options
    shell = ""
    if group == "office":
        shell = "/bin/bash" #"/bin/csh" cannot find csh on my system so changing to bash for testing but works none the less
    else:
        shell = "/bin/bash"

    try:
        subprocess.run(['sudo', 'useradd', '-p', default_pass, '-d', "/home/" + dept.lower() + "/" + username, '-s', shell, '-u', id, '-g', group, username]) #index user name on csv file
        os.system("sudo passwd --expire " + username)
    except:
        print("Could not add user")

def create_user_name(first, last):
    user_name = (first[:1] + last).lower().replace("'", "")
    #check for duplicate names
    for user in users:
        if user_name == user: #if match
            user_name += "1"
    users.append(user_name)
    return user_name

#Clear Console
os.system("clear")

print("Adding new users to the system...")
print("---------------------------------")
print()

#Reading csv file
with open(users_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

#itterate over users
for row in rows:
    print("Processing employee ID " + row[0])

    if (row[2] == ""):
        print("Not enough information for user id: " + row[0])
        continue

    if (row[6] == "area51"):
        print("Invalid User Group for user id: " + row[0])
        continue

    try:
        os.system("sudo groupadd " + row[6])
    except:
        print("Group exists")

    current_user = create_user_name(row[2], row[1])
    add_user(current_user, row[0], row[3], row[4], row[5], row[6])

    print("Added user: " + current_user)    

#End and output
print()
print("---------------------------------")
print()
print("All users with valid information have been added: ")
for user in users:
    print(user)

print()
print("Default Password: " + default_pass)
