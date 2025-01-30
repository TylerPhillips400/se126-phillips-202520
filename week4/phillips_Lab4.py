#Tyler Phillips
#SE126.04
#Lab 4
#1-30-2025

#PROMPT:
#PART 1: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.
#PART 2: 

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#fName
#lName
#age
#sName
#house

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

#--connected to file------------------------------------------
with open("week4/got_emails.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        house.append(rec[4])

#--disconnected from file---------------------------------------