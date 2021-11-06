#PADEN JOHNSON 
#10/18/2021

#!/usr/bin/env/python3

import os
import subprocess

user_choice = ""
srcpath = ""
dstpath = ""
found_links = []

#Functions

def create_link():
    srcpath = input("Enter filepath for file you'd like to link: ")
    exists = os.path.exists(srcpath)
    if (exists):
        dstpath = input("Enter destination for linked file: ")
        os.symlink(srcpath, dstpath)
        print("Link created.")
    else:
        print("File does not exist... ")

def delete_link():
    srcpath = input("Enter filepath for linked file you'd like to remove: ")
    exists = os.path.exists(srcpath)
    if (exists):
        os.unlink(srcpath)
        print("File Unlinked.")
    else:
        print("File does not exist... ")

def summary_report():
    print("Generating summary report... ")

    #loop through directory and os.islink, add each to array
    for file in os.listdir(os.path.expanduser('~')):
        if (os.path.islink(os.path.expanduser('~') + "/" + file)): #had to add the .. path to the file
            found_links.append(file) #If file is link, add to array

    #Printing Report
    print()
    print("- REPORT -")
    print()

    for x in found_links:
        print(x)

    print("Total number of links: " + str(len(found_links)))

    #reset list for another run if needed
    del found_links[:]

#Clear Console
os.system("clear")

#print current directory
print("Current Directory: ")
print(os.getcwd())

#main loop until user enters quit
#Create, delete, or summary report

print()
print("- SYM LINK MANAGER -")
print()

while (user_choice.lower() != "quit"):
    print("1. Create a Sym Link")
    print("2. Delete a Sym Link")
    print("3. Summary Report")

    user_choice = input("Enter the corresponding number to select an option: ")

    if (user_choice == "1"):
        print("Create Sym Link")
        create_link()

    elif (user_choice == "2"):
        print("Delete Sym Link")
        delete_link()

    elif (user_choice == "3"):
        print("Summary report")
        summary_report()
    else:
        print()