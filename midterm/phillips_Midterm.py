#Tyler Phillips
#SE126.04
#Midterm Choice 1
#2-10-2025

#PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#fName              List for first name from CSV file
#lName              List for last name from CSV file
#dep                List for department from CSV file
#phoneExt           List for phone extension from CSV file
#email              List for email from CSV file
#officeNum          List for office room number based on counting variable num
#num                Counting variable starting at 100
#answer             While answer = "y" the program will allow you to search again
#search_type        Type of search based on what the user types [input]
#found              List for all found indexs based on the search
#search_email       Asks the user what email they would like to search for [input]
#search_dep         Asks the user what department they would like to search for [input]

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
fName = []
lName = [] 
email = []
dep = []
phoneExt = []
officeNum = []      #New List

#Counting variable
num = 99

#--connected to file------------------------------------------
with open("Midterm/westeros.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        num += 1
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        dep.append(rec[3])
        phoneExt.append(rec[4])
        officeNum.append(num)

#--disconnected from file---------------------------------------

#Labels for Data
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':5} {'OFFICE #'}")
print("--------------------------------------------------------------------------------------------------")

#just printing
for i in range(0, len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dep[i]:23} {phoneExt[i]:5} {officeNum[i]}")

print("--------------------------------------------------------------------------------------------------")

#WRITING NEW DATA
file = open("midterm/midterm_choice1.csv", "w")

for i in range(0, len(fName)):
    if i in range(0, 16):
        file.write(f"{fName[i]},{lName[i]},{email[i]},{dep[i]},{phoneExt[i]},{officeNum[i]}\n")
    else:   #So that there is no extra line created in the CSV file
        file.write(f"{fName[i]},{lName[i]},{email[i]},{dep[i]},{phoneExt[i]},{officeNum[i]}")
file.close()    #Closing new file created
print(f"\n{len(fName)} records processed and put in to midterm_choice1.csv")

#SEQUENTIAL SEARCH-------------------------------------------------------------------
answer = "y"
#SEARCH MENU
while answer == "y":
    print("\n\t~SEARCH MENU~")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT")

    search_type = input("\nEnter your search type [1-3]: ")

    while search_type != "1" and search_type != "2" and search_type != "3": #Trap for invaild entrys
        print("\t!INVALID ENTRY!")
        search_type = input("\nEnter your search type [1-3]: ")


    #filter search options based on type
    if search_type == "1": #EMAIL
        
        print("\n\tEMAIL SEARCH~")

        found = []
        search_email = input("Enter the EMAIL you wish to find: ") 

        for i in range(0, len(email)):
            if search_email.lower() in email[i].lower():
                found.append(i)
                print(f"Found {search_email.title()} at INDEX {i}")

        if not found:       #NOT FOUND
            print(f"Your search for {search_email.title()} was NOT FOUND!")
        else:               #FOUND
            print(f"\nYour search for {search_email.title()} was FOUND! Here is the data: ")
            print(f"  {'#':3} {'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':5} {'OFFICE #'}")
            print("--------------------------------------------------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{found[i]:3}:  {fName[found[i]]:8} {lName[found[i]]:10} {email[found[i]]:30} {dep[found[i]]:23} {phoneExt[found[i]]:5} {officeNum[found[i]]}")
            print("--------------------------------------------------------------------------------------------------")
    
    elif search_type == "2": #DEPARTMENT
        print("\n\tDEPARTMENT SEARCH")

        found = []  
        search_dep = input("Enter the DEPARTMENT you wish to find: ")

        for i in range(0, len(dep)):
            if search_dep.lower() in dep[i].lower():
                found.append(i)
                print(f"Found {search_dep.title()} DEPARTMENT at INDEX {i}")

        if not found:       #NOT FOUND
            print(f"Your search for {search_dep.title()} was NOT FOUND!")
        else:               #FOUND
            print(f"\nYour search for {search_dep.title()} was FOUND! Here is the data: ")
            print(f"  {'#':3} {'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':5} {'OFFICE #'}")
            print("--------------------------------------------------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{found[i]:3}:  {fName[found[i]]:8} {lName[found[i]]:10} {email[found[i]]:30} {dep[found[i]]:23} {phoneExt[found[i]]:5} {officeNum[found[i]]}")
            print("--------------------------------------------------------------------------------------------------")
    elif search_type == "3": #EXIT
        print("\t~EXIT~")
        answer = "x"

    if search_type == "1" or search_type == "2":
        answer = input("\nWould you like to search again? [y/n]: ").lower()


#Final print statement
print("\nThanks for using the program! Goodbye")

    