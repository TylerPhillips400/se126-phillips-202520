#W4D1 - Sequential Search

#Prompt: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

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

def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let      #The value stored to let will literally replace the letter() call in main code

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Create some empty lists - one list for every potential field in the file
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

#--connected to file------------------------------------------
with open("week3/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #Store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists. conneceted by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#--disconnected from file---------------------------------------

#Process the lists to create and store each student's numeric average as well as letter grade average, then display all data back to the user

num_avg = []       #Holds student's numeric avg: (test1 + test2 + test3) / 3
let_avg = []       #Holds student's letter avg: letter(num_avg) return

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

#print field headers for display below
print(f"\n{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6} {'L AVG'}")
print("--------------------------------------------------------------------------------------")
#Processing through lists for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3} {num_avg[i]:6.1f}   {let_avg[i]}")

print("--------------------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE: {len(firstName)}")

#Sequential Search - search for a student by their last name

#Step 1: set-up and gain search query
found = -1      #flag var, will be replaced with index position if name is found
search_last = input("\nEnter the last name you wish to find: ")       #name we are looking for

#Step 2: Preform search algo (seq. search -> for loop w/ if statement)
for i in range(0, len(lastName)):
    #For loop preforms the SEQUENCE - from start thoguh end of list items

    if search_last.lower() == lastName[i].lower():
        #if preforms the SEARCH - is what we're looking for here in the list?
        found = i   #Stores found item's INDEX LOCATION

#Step 3: Display results to user; make sure you give info: both for found and NOT found
if found != -1:
    #Last name FOUND!
    print(f"\nYour search for {search_last.title()} was FOUND! Here is their data: ")
    print(f"\n{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6} {'L AVG'}")
    print("--------------------------------------------------------------------------------------")
    print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3} {num_avg[found]:6.1f}   {let_avg[found]}\n\n")
else:
    #NOT found
    print(f"\nYour search for {search_last.title()} was NOT FOUND!\n\n")

