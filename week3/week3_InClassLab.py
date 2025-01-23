#Tyler Phillips
#SE126.04
#W3 In Class lab 
#1-23-2025

#PROGRAM PROMPT: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#VARIABLE DICTIONARY
#total_rec          Total number of computers / records processed
#csvfile            Variable that opens the CSV file attached to the relative path
#file               Passes the CSV file through the reader function and is stored to this variable
#rec                Variable that represents each record in the CSV file
#type               Type of device in record
#brand              Brand of device in record
#cpu                Type of CPU in device
#ram                Amount of ram in device
#disk1              Amount of spance in disk 1
#numHDDS            Number of HDDS in device
#disk2              Amount of spance in disk 2
#os                 What version OS device is running
#year               Year device was made

#--------IMPORTS----------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library
import csv
#--------FUNCTIONS--------------------------------------------
def clear():    #<--FUNCTION HEADER
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

#--------MAIN EXECUTING CODE----------------------------------

clear()     #Clear Terminal

total_rec = 0

#--connected to file------------------------------------------
with open("week2/filehandling.csv") as csvfile:

    #Reader function to read csvfile
    file = csv.reader(csvfile)

    #Labels for Data
    print(f"{'TYPE':10}  {'BRAND':10} {'CPU':5}   {'RAM':5}   {'1st Disk':10} {'No HDDS':10}   {'2nd Disk':10} {'OS'}   {'YR'}")
    print("--------------------------------------------------------------------------------------------------")
    
    for rec in file:

        #Counting Variable
        total_rec += 1
        
        #Converting If Statements
        type = rec[0]
        if type == "D":
            type = "Desktop"
        else:
            type = "Laptop"

        brand = rec[1]
        if brand == "DL":
            brand = "Dell"
        elif brand == "GW":
            brand = "Gateway"
        
        #Record storing to variables
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        numHDDs = rec[5]

        #Allowing processor to process different amount of fields in each record
        if numHDDs == "1":
            disk2 = "-----"
            os = rec[6]
            year = rec[7]
        else:
            disk2 = rec[6]
            os = rec[7]
            year = rec[8]
        
        print(f"{type:10}  {brand:10} {cpu:5}   {ram:5}   {disk1:10} {numHDDs:10}   {disk2:10} {os}  {year}")


    
        
        
#--disconnected from file---------------------------------------
#Final print statements
print("--------------------------------------------------------------------------------------------------")
print(f"{total_rec} Computers processed")
