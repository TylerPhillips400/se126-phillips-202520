#Tyler Phillips
#SE126.04
#Lab 2
#1-16-2025

#PROGRAM PROMPT: 

#VARIABLE DICTIONARY

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

    file = csv.reader(csvfile)

    print(f"{'NAME':20}     {'MAX':5}   {'PPL':5}   {"OVER":5}")
    print("-------------------------------------------------")
    
    for rec in file:

        total_rec += 1
        
        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        numHDDs = rec[5]
        os = rec[7]
        year = rec[8]

        if numHDDs == 2:
            disk2 = rec[6]
        else:
            disk2 = "-----"

    
        
        
#--disconnected from file---------------------------------------
print("-------------------------------------------------")
print(f"TOTAL RECORDS: {total_rec}")
