#W4D2 - Sequential Search Review + Creating & Writing to Text Files

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

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

clear()

#Create some empty lists - one list for every potential field in the file
dragons = []        #field 0 - Dragon names
riders = []         #field 1 - Rider names
counts = []         #field 2* - 1 or 2, count of colors
color1 = []         #First primary color
color2 = []         #second color, only when count is 2


#--connected to file------------------------------------------
with open("week4/dragons.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        dragons.append(rec[0])
        riders.append(rec[1])
        counts.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        else:
            color2.append("-----")

#--disconnected from file---------------------------------------

#print field headers for display below
print(f"\n{'DRAGONS':15}  {'RIDERS':30}   {'#':3}   {'COLOR 1':8}   {'COLOR 2'}")
print("--------------------------------------------------------------------------------------")
#Processing through lists for display
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}  {riders[i]:30} {counts[i]:3}     {color1[i]:8}   {color2[i]}")

print("--------------------------------------------------------------------------------------")
print(f"TOTAL RECORDS IN FILE: {len(dragons)}")

#SEARCH FOR A SPECIFIC DRAGON
#step 1: set up and gain of search
found = "x"
search = input("Which Dragon are you looking for: ")

#Step 2: preform search --> loop w/ if statement
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():            #<-----               If search term is in the value of dragons
        #hold onto the found location (index) of our searched-for value
        found = i

#Step 3: filter and display results
if found != "x":
    print(f"\nYour search for {search.title()} has been FOUND: ")
    print(f"\n{'DRAGONS':15}  {'RIDERS':30}   {'#':3}   {'COLOR 1':8}   {'COLOR 2'}")
    print("--------------------------------------------------------------------------------------")
    print(f"{dragons[found]:15}  {riders[found]:30}   {counts[found]:3}   {color1[found]:8}   {color2[found]}")
else:
    print(f"Your search for {search.title()} was NOT FOUND :[")


#SEARCH FOR A COLOR SET
found = []
search = input("Enter the color you are looking for: ")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

print("\nHere is what the found list contains")
for i in range(0, len(found)):
    print(f"\t{found[i]}")

if not found:       #"If the found list is empty"
    print(f"Your search for {search.title()} was NOT FOUND :[")
else:
    print(f"\n{'DRAGONS':15}  {'RIDERS':30}   {'#':3}   {'COLOR 1':8}   {'COLOR 2'}")
    print("--------------------------------------------------------------------------------------")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15}  {riders[found[i]]:30}   {counts[found[i]]:3}   {color1[found[i]]:8}   {color2[found[i]]}")


#WRITE SOME DATA TO A FILE + CREATING SAID FILE
#create and write dragons and riders of the data to a new text file
file = open("week4/targs.csv", "w")

for i in range(0, len(dragons)):
    if i in range(0, 14):
        file.write(f"{dragons[i]},{riders[i]}\n")
    else:
        #elif i in range(15):
        file.write(f"{dragons[i]},{riders[i]}")
file.close()

#NEED AN IF STATEMENT TO MAKE THE LAST LINE IN THE CSV FILE TO NOT BE EMPTY
#   ~If i in range(15)

targs1 = []
targs2 = []


with open("week4/targs.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        targs1.append(rec[0])
        targs2.append(rec[1])

print(f"\n{'DRAGONS':15}  {'RIDERS'}")
print("--------------------------------------------------------------------------------------")
#Processing through lists for display
for i in range(0, len(dragons)):
    print(f"{targs1[i]:15}  {targs2[i]}")

print("--------------------------------------------------------------------------------------")
print(f"TOTAL RECORDS IN FILE: {len(targs1)}")

#NEED AN IF STATEMENT TO MAKE THE LAST LINE IN THE CSV FILE TO NOT BE EMPTY
#   ~If i in range(15)