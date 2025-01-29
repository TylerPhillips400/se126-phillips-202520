#Tyler Phillips
#SE126.04
#W4 In Class Lab
#1-27-2025

#Prompt: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

#VARIABLE DICTIONARY
#num                Passed number from variable in main code
#let                Letter grade that corresponds to an average number grade
#firstName          First name from the CSV file appended into a list
#lastName           Last name from the CSV file appended into a list
#test1              1st test score from the CSV file appended into a list
#test2              2nd test score from the CSV file appended into a list
#test3              3rd test score from the CSV file appended into a list
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#num_avg            Average number grade using variable a as the average appended into a list
#let_avg            Average letter grade using letter() appended into a list
#i                  Index of each field of data from all records
#a                  Variable used to calculate the average number grade
#answer             Answer starts as "y" and prompts the user if they want to search again [input]
#search_type        Asks the user what parameter they would like to search from [input]
#search_last        Asks the user what last name they want to search for [input]
#search_first       Asks the user what first name they want to search for [input]
#search_let         Asks the user what letter grade they want to search for [input]
#found              Starts at -1 and if data is found it stores the index(s) of found data

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

def letter(num):        #Finding the average letter grade
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


#SEQUENTIAL SEARCH-------------------------------------------------------------------
print("\n\tWelcome to the Student Search Program")

answer = input("Would you like to start your search? [y/n]: ").lower()

while answer == "y":
    #show user search menu 
    print("\n\t~Search Menu~")
    print("1. Search by LAST name")         #one search value 
    print("2. Search by FIRST name")        #one search value 
    print("3. Search by LETTER grade")      #multiple search values
    print("4. EXIT")
    
    search_type = input("\nEnter your search type [1-4]: ")

    if search_type == "1": #LAST NAME
        
        print("\n\tLAST NAME SEARCH~")

        found = -1 
        search_last = input("Enter the last name you wish to find: ") 

        for i in range(0, len(lastName)):

            if search_last.lower() == lastName[i].lower(): 
                found = i  

        if found != -1:
            print(f"Your search for {search_last.title()} was FOUND! Here is their data: ")
            #print field headers for display below
            print(f"\n{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6} {'L AVG'}")
            print("--------------------------------------------------------------------------------------")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            print(f"Your search for {search_last.title()} was NOT FOUND!")
    
    elif search_type == "2": #LAST NAME
        
        print("\n\tFIRST NAME SEARCH~")

        found = -1  
        search_first = input("Enter the last name you wish to find: ") 

        for i in range(0, len(firstName)):

            if search_first.lower() == firstName[i].lower(): 
                found = i 

        if found != -1:
            print(f"Your search for {search_first.title()} was FOUND! Here is their data: ")
            #print field headers for display below
            print(f"\n{'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6} {'L AVG'}")
            print("--------------------------------------------------------------------------------------")
            print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
        else: 
            print(f"Your search for {search_first.title()} was NOT FOUND!")
    
    elif search_type == "3": #LETTER GRADE
        print("\n\tLETTER GRADE SEARCH")

        found = [] 
        search_let= input("Enter the LETTER GRADE you wish to find: ") 

        for i in range(0, len(let_avg)):
    
            if search_let.upper() == let_avg[i]: 
                found.append(i)  
                print(f"\nFound a {search_let.title()} grade in INDEX {i}")

        if not found: 
            print(f"Your search for {search_let.title()} was NOT FOUND!")
        else: 
            print(f"Your search for {search_let.title()} was FOUND! Here is their data: ")
            #print field headers for display below
            print(f"\n{'INDEX':5}   {'FIRST':10}  {'LAST':10}   {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6} {'L AVG'}")
            print("--------------------------------------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{found[i]:5}:  {firstName[found[i]]:10}  {lastName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_avg[found[i]]}")
    elif search_type == "4": #exit
        print("\n\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop
    if search_type == "1" or search_type == "2" or search_type == "3":

        answer = input("\nWould you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")