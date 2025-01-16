#Tyler Phillips
#SE126.04
#W2D2 in Class Lab - Text File Handling Review
#1-16-2025

#PROGRAM PROMPT: The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY
#people             The amount of people attending that will be passed through the difference function
#max_cap            The maximum capacity of the room that will be passed through the difference functiom
#diff               The difference of the max capacity and the amount of people attending
#total_rec          The total amount of records processed
#rooms_over         The amount of rooms that are over max capacity
#csvfile            Opens CSV file and stores to this variable
#file               Reads csvfle and stores to this variable
#rec                Records that are in the file
#name               Name of the room the meeting will be at
#max                The rooms max capacity
#ppl                The amoount of people attending
#remaining          the difference of the max capacity and people attending

#--------IMPORTS----------------------------------------------
#Import os for clear() function
from os import name, system
#import the CSV (comma separated value) library
import csv
#--------FUNCTIONS--------------------------------------------
def clear():    
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

def difference(people, max_cap):
    '''This function is passed 2 values and returns the difference between them'''
    diff = max_cap - people

    return diff     #this value will replace the difference() call in the main code

#--------MAIN EXECUTING CODE----------------------------------

clear()     #Clear Terminal

#initialize needed counting vars
total_rec = 0
rooms_over = 0

#--connected to file------------------------------------------
with open("week2/classLab2.csv") as csvfile:
    #We must indent one level while connected to the file

    file = csv.reader(csvfile)

    print(f"{'NAME':20}     {'MAX':5}   {'PPL':5}   {"OVER":5}")
    print("-------------------------------------------------")
    
    for rec in file:
        #below code occurs for every record (row) in the file (textfile -> 2D list!)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])       #All text data read as a string; so cast as a num!
        ppl = int(rec[2])

        #call the difference() to find people over / under capacity
        remaining = difference(ppl, max)

        #count and display the rooms that are over capacity (remaining value is negative)
        if remaining < 0:
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")
        
        #count ALL rooms!
        total_rec += 1
        
#--disconnected from file---------------------------------------
#display final data (counting vars)
print("-------------------------------------------------")
print(f"\nRooms currently OVER capacity: {rooms_over}")
print(f"      Total rooms in the file: {total_rec}\n")