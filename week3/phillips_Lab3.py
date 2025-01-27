#Tyler Phillips
#SE126.04
#Lab 3
#1-23-2025

#PROGRAM PROMPT: Construct a program that will analyze potential voters. The program should generate the following totals: Number of individuals not eligible to register. Number of individuals who are old enough to vote but have not registered. Number of individuals who are eligible to vote but did not vote. Number of individuals who did vote. Number of records processed.

#VARIABLE DICTIONARY
#idnum              Appened list of all ID numbers in the CSV file
#age                Appened list of all the ages in the CSV file
#reg                Appened list of if the person is registerd from the CSV file
#vote               Appened list of if the person voted from the CSV file
#total_rec          The total amount of records counted from the CSV file
#cannot_reg         Total amount of people that are not of age so they cant register
#not_reg            Total amount of people that are of age but havent registered
#no_vote            Total amount of people that are registered but didnt vote
#voted              Total amount of people that voted
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records

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

#Empty Lists for records
idnum = []      #ID number
age = []        #Age of voter
reg = []        #Is voter registered
vote = []       #Did the person vote

#counting variables
total_rec = 0
cannot_reg = 0
not_reg = 0
no_vote = 0
voted = 0

#--connected to file------------------------------------------
with open("week3/voters_202040.csv") as csvfile:

    #Reader function to read csvfile
    file = csv.reader(csvfile)
    
    for rec in file:

        #Appending the lists with each field from the records
        idnum.append(rec[0])
        age.append(rec[1])
        reg.append(rec[2])
        vote.append(rec[3])

        total_rec += 1

#--disconnected from file---------------------------------------

#Labels for Data
print(f"{'ID #'}  {'AGE'} {'REGISTERED'}   {'VOTED':5}")
print("--------------------------------------------------------------------------------------------------")

#just printing
for i in range(0, len(idnum)):
    print(f"{idnum[i]}  {age[i]}  {reg[i]}            {vote[i]}")

print("--------------------------------------------------------------------------------------------------")

#Processing if voter is of age, registered, and if they voted
for i in range(0, len(age)):
    if int(age[i]) < 18:
        cannot_reg += 1
    else:
        if reg[i] == "N":
            not_reg += 1
        else:
            if vote[i] == "N":
                no_vote += 1
            else:
                voted += 1


#Final Print statements
print(f"         Not able to register: {cannot_reg}")
print(f"Old enough but not registered: {not_reg}")
print(f"   Regsitered but didn't vote: {no_vote}")
print(f"                 Amount voted: {voted}")
print(f"  Amount of Records Processed: {total_rec}")