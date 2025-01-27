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

#CREATE AN EMPTY LIST for every *potential* field in the file
#Always base your number of lists on the longest record ie the one with the most field data
comptype = []       #Computer type -> D or L
manu = []           #Manufacturer -> DL, GW, or HP
proc = []           #Processor type
ram = []            #Total RAM
hd_1 = []           #Hard drive #1

num_hd = []         #Hard drive #2 * even though not all records have this,  still create an empty list

hd_2 = []           
os = []             #Operating system
yr = []             #Machine year

#total_rec = 0

#--connected to file------------------------------------------
with open("week2/filehandling.csv") as csvfile:

    #Reader function to read csvfile
    file = csv.reader(csvfile)
    
    for rec in file:

        #Counting Variable
        #total_rec += 1
        
        if rec[0] == "D":
            comptype.append("Desktop")
        else:
            comptype.append("Laptop")

        if rec[1] == "DL":
            manu.append("Dell")
        elif rec[1] == "GW":
            manu.append("Gateway")
        else:
            manu.append("HP")
        
        proc.append(rec[2])
        ram.append(rec[3])
        hd_1.append(rec[4])
        num_hd.append(rec[5])

        #Allowing processor to process different amount of fields in each record
        if rec[5] == "1":
            hd_2.append("-----")
            os.append(rec[6])
            yr.append(rec[7])
        else:
            hd_2.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        
        #print(f"{type:10}  {brand:10} {cpu:5}   {ram:5}   {disk1:10} {numHDDs:10}   {disk2:10} {os}  {year}")



#--disconnected from file---------------------------------------
#print(f"{total_rec} Computers processed")

#process data from lists using a FOR loop *after* you are no longer connected to the file

#Labels for Data
print(f"{'TYPE':10}  {'BRAND':10} {'CPU':5}   {'RAM':5}   {'1st Disk':10} {'No HDDS':10}   {'2nd Disk':10} {'OS'}   {'YR'}")
print("--------------------------------------------------------------------------------------------------")

#just printing
for i in range(0, len(comptype)):
    print(f"{comptype[i]:10}  {manu[i]:10} {proc[i]:5}   {ram[i]:5}   {hd_1[i]:10} {num_hd[i]:10}   {hd_2[i]:10} {os[i]}  {yr[i]}")

print("--------------------------------------------------------------------------------------------------")
#counting for desktops and laptops that are old
old_desk = 0        #from 2016 or earlier
old_lap = 0

for i in range(0, len(yr)):

    if int(yr[i]) <= 16: #Too old
        print(f"old machine found om index {i}")
        if comptype[i] == "Desktop":
            old_desk += 1
        elif comptype[i] == "Laptop":
            old_lap += 1
    

#Final print statements
print(f"\nTo replace {old_desk} it will cost ${old_desk * 2000:6}")
print(f"To replace {old_lap} it will cost ${old_lap * 1500:6}")

input("Press ant key to continue... ")

print("\nThank you for using the program. Goodbye!")