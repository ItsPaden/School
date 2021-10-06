#PADEN JOHNSON 
#10/1/2021

#!/usr/bin/env python3

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
        shell = "csh"
    else:
        shell = "bash"

    try:
        subprocess.run(['useradd', '-p', default_pass, '-d', "/home/" + dept.lower() + "/" + username, '-s', shell, '-u', id, username]) #index user name on csv file
        os.system("passwd --expire" + username)
    except:
        print("Could not add user")

def create_user_name(first, last):
    user_name = (first[:1] + last).lower().replace("'", "")
    #check for duplicate names
    for user in users:
        if user_name == user:
            user_name += "1"
    users.append(user_name)
    return user_name

#Clear Console
#os.system("clear")

print("Adding new users to the system...")
print("Default Password: " + default_pass)

#Reading csv file
with open(users_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

#itterate over users
for row in rows:
    print("Processing employee ID " + row[0])

    if (row[6] != "pubsafety" or row[6] != "office"):
        print("Invalid User Group for " + row[0])
        continue

    try:
        os.system("group add " + row[6])
    except:
        print("Group exists")

    current_user = create_user_name(row[2], row[1])
    add_user(current_user, row[0], row[3], row[4], row[5], row[6])

    print("Added user: " + current_user)    

