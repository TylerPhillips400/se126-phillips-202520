#Tyler Phillips
#SE126.04
#Lab 5
#2-21-2025

#PROMPT: Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. The program should display the seat pattern, with an ‘X’ making the seats already assigned. After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#answer             Asks user for their answer to rerun the program [input]
#dataFile           Variable storing the CSV file into a 2D list
#numList            List for each row number using num
#num                Counting variable for numList
#ans                Answer for if the program will rerun
#row                Asks user for what row they would like to reserve a seat in [input]
#seat               Asks user what seat they would like to reserve [input]

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

def display():      #Prints full display
    print(f"\n{'Row #':5}    {'A':3} {'B':7} {'C':3} {'D'}")
    print("---------------------------------------------------------------------------------------------")
    for i in range(0, len(dataFile)):
            print(f"{numList[i]:5}    {dataFile[i][0]:3} {dataFile[i][1]:7} {dataFile[i][2]:3} {dataFile[i][3]}") 
    print("---------------------------------------------------------------------------------------------") 

def ansCheck():     #Answer check and loop
    answer = input("\nWould you like to reserve annother seat? [y/n]: ").lower()
    while answer != 'y' and answer != 'n':
        print("***Invaild Input***")
        answer = input("\nWould you like to reserve annother seat? [y/n]: ").lower()
    
    return answer

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
dataFile = []
numList = []

#Counting variables
num = 0

#--connected to file------------------------------------------
with open("week7/airplane.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        num += 1    #Counts each record
        numList.append(num)     #Stores each number to a list for numbering rows
        dataFile.append(rec)    #2D List
#--disconnected from file---------------------------------------
print("Welcome to the airplane seating reserve program\nBelow is the current layout:\n")
display()   #Starting display
ans = "y"

while ans == "y":       #Program loop
    row = int(input("\nWhich row would you like to reserve a seat in: "))
    while row not in [1, 2, 3, 4, 5, 6, 7]: #Trap loop
        print("***Invaild Input***")
        row = int(input("\nWhich row would you like to reserve a seat in: "))
    seat = input("Which seat would you like to reserve: ").upper()
    while seat not in ['A', 'B', 'C', 'D']: #Trap loop
        print("***Invaild Input***")
        seat = input("Which seat would you like to reserve: ").upper()

    #dataFile manipulation
    if row == 1:        #ROW 1
        if seat == 'A':
            dataFile[0][0] = 'X'
        elif seat == 'B':
            dataFile[0][1] = 'X'
        elif seat == 'C':
            dataFile[0][2] = 'X'
        elif seat == 'D':
            dataFile[0][3] = 'X'
    elif row == 2:      #ROW 2
        if seat == 'A':
            dataFile[1][0] = 'X'
        elif seat == 'B':
            dataFile[1][1] = 'X'
        elif seat == 'C':
            dataFile[1][2] = 'X'
        elif seat == 'D':
            dataFile[1][3] = 'X'
    elif row == 3:      #ROW 3
        if seat == 'A':
            dataFile[2][0] = 'X'
        elif seat == 'B':
            dataFile[2][1] = 'X'
        elif seat == 'C':
            dataFile[2][2] = 'X'
        elif seat == 'D':
            dataFile[2][3] = 'X'
    elif row == 4:      #ROW 4
        if seat == 'A':
            dataFile[3][0] = 'X'
        elif seat == 'B':
            dataFile[3][1] = 'X'
        elif seat == 'C':
            dataFile[3][2] = 'X'
        elif seat == 'D':
            dataFile[3][3] = 'X'
    elif row == 5:      #ROW 5
        if seat == 'A':
            dataFile[4][0] = 'X'
        elif seat == 'B':
            dataFile[4][1] = 'X'
        elif seat == 'C':
            dataFile[4][2] = 'X'
        elif seat == 'D':
            dataFile[4][3] = 'X'
    elif row == 6:      #ROW 6
        if seat == 'A':
            dataFile[5][0] = 'X'
        elif seat == 'B':
            dataFile[5][1] = 'X'
        elif seat == 'C':
            dataFile[5][2] = 'X'
        elif seat == 'D':
            dataFile[5][3] = 'X'
    elif row == 7:      #ROW 7
        if seat == 'A':
            dataFile[6][0] = 'X'
        elif seat == 'B':
            dataFile[6][1] = 'X'
        elif seat == 'C':
            dataFile[6][2] = 'X'
        elif seat == 'D':
            dataFile[6][3] = 'X'

    #Invaild answer trap loop
    ans = ansCheck()

#Final Display
print()
display()

#Final print statement
print(f"\n\nThank you for using the program! Goodbye")