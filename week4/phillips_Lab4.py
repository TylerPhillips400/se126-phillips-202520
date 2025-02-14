#Tyler Phillips
#SE126.04
#Lab 4
#1-30-2025

#PROMPT:
#PART 1: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.
#PART 2: Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. Note: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file).

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#fName              List for first name from CSV file
#lName              List for last name from CSV file
#age                List for age from CSV file
#sName              List for screen name from CSV file
#house              List for house allegiance from CSV file
#dep                List for department based on house allegiance
#phoneExt           List for phone extension based on department
#ext1               Counting variable for ext 100 - 199
#ext2               Counting variable for ext 200 - 299
#ext3               Counting variable for ext 300 - 399
#ext4               Counting variable for ext 400 - 499
#ext5               Counting variable for ext 500 - 599
#ext6               Counting variable for ext 600 - 699
#email              List for email based e variable calculation
#e                  screen name plus @westeros.net

#-Imports-------------------------------------------------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library
import csv
#-Functions-----------------------------------------------------------------------------------
def clear():
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
fName = []      #Unique
lName = []
age = []
sName = []      #Unique
house = []
dep = []
phoneExt = []   #Unique

#Counting vsriables
ext1 = 99
ext2 = 199
ext3 = 299
ext4 = 399
ext5 = 499
ext6 = 599

#--connected to file------------------------------------------
with open("week4/got_emails.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        house.append(rec[4])

        #Departement and Phone Ext list conditions based on house
        if rec[4] == "House Stark":
            dep.append("Research & Development")
            ext1 += 1
            phoneExt.append(ext1)
        elif rec[4] == "House Targaryen":
            dep.append("Marketing")
            ext2 += 1
            phoneExt.append(ext2)
        elif rec[4] == "House Tully":
            dep.append("Human Resources")
            ext3 += 1
            phoneExt.append(ext3)
        elif rec[4] == "House Lannister":
            dep.append("Accounting")
            ext4 += 1
            phoneExt.append(ext4)
        elif rec[4] == "House Baratheon":
            dep.append("Sales")
            ext5 += 1
            phoneExt.append(ext5)
        else:
            dep.append("Auditing")
            ext6 += 1
            phoneExt.append(ext6)

#--disconnected from file---------------------------------------

#Email list creation
email = []
for i in range (0, len(sName)):
    e = sName[i] + "@westeros.net"
    email.append(e)

#Labels for Data
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("--------------------------------------------------------------------------------------------------")

#just printing
for i in range(0, len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dep[i]:23} {phoneExt[i]:3}")

print("--------------------------------------------------------------------------------------------------")

#WRITING NEW DATA
file = open("week4/westeros1.csv", "w")

for i in range(0, len(fName)):
    if i in range(0, 16):
        file.write(f"{fName[i]},{lName[i]},{email[i]},{dep[i]},{phoneExt[i]}\n")
    else:   #So that there is no extra line created in the CSV file
        file.write(f"{fName[i]},{lName[i]},{email[i]},{dep[i]},{phoneExt[i]}")
file.close()    #Closing new file created

#Final print statement
print(f"\n\n{len(fName)} records processed and made into the new westeros.csv file")