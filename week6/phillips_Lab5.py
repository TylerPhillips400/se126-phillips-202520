#Tyler Phillips
#SE126.04
#Lab 5
#2-14-2025

#PROMPT: Build a personal library search system using the file book_list.csv. Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#x                  Index for display() function
#records            Amount of records that are being passed through the display() function
#libNum             List of all library numbers from CSV file
#title              List of all titles from CSV file
#author             List of all authors from CSV file
#genre              List of all genres from CSV file
#pCount             List of all page counts from CSV file
#status             Status of all books in a list from CSV file
#found              Found list for if a search is found within the CSV file
#listname           list name for the swap() to bubble sort
#temp               temp variable for bubble sort swap()
#avail              List of all available books from CSV file
#loan               List of all on loan books from CSV file
#ans                Answer from while loop and entering the search program [input]
#search_type        The type of search the user chooses [input]
#search             The search that the user will be entering [input]

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

def display(x, records):
    print(f"{'#':5}  {'TITLE':33}   {'AUTHOR':15}  {'GENRE':15}  {'P #s':5}  {'STATUS'}")
    print("---------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{libNum[x]:5} {title[x]:33}   {author[x]:15}  {genre[x]:15}  {pCount[x]:5}  {status[x]}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{libNum[found[i]]:5}  {title[found[i]]:33}   {author[found[i]]:15}  {genre[found[i]]:15}  {pCount[found[i]]:5}  {status[found[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{libNum[i]:5}  {title[i]:33}   {author[i]:15}  {genre[i]:15}  {pCount[i]:5}  {status[i]}")
    print("---------------------------------------------------------------------------------------------")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
libNum = []
title = []
author = []
genre = []
pCount = []
status = []

avail = []
loan = []

found = []

#--connected to file------------------------------------------
with open("week6/book_list.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        libNum.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pCount.append(rec[4])
        status.append(rec[5])

        if rec[5] == "available":   #Sorts rec[5] or on loan or available
            avail.append(rec[5])
        else:
            loan.append(rec[5])


#--disconnected from file---------------------------------------

ans = input("\nWould you like to enter the search program? [y/n]: ").lower()

#Error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    found = []  #RESET found[]

    print("\tSEARCHING MENU")
    print("1. Show All TITLES")         #   |   Alphabetical
    print("2. Show All AVAILABLE")      #   |-------- SHOW ALL
    print("3. Show All ON LOAN")        #   |
    print("4. Search by TITLE")         #Keyword search
    print("5. Search by AUTHOR")        #
    print("6. Search by GENRE")         #
    print("7. Search by LIBRARY #")     #Binary search
    print("8. EXIT")    #EXIT

    search_type = input("\nHow would you like to search today? [1-8]: ")

#using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":    #SHOW ALL TITLES
        #BUBBLE SORT: ALPHABETICAL SORTING
        for i in range(0, len(title) - 1):
            for j in range(0, len(title) - 1):
                if title[j] > title[j + 1]:
                    swap(j, libNum)
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pCount)
                    swap(j, status)
        display("x",len(title))
        input("\nPress any key to continue...")
       
    elif search_type == "2":    #SHOW ALL AVAILABLE
        print(f"{'TITLE':33} {'AVAILABLE'}")
        print("---------------------------------------------")
        for i in range(len(avail)):
            print(f"{title[i]:33} {avail[i]}")
        print("---------------------------------------------")
        input("\nPress any key to continue...")

    elif search_type == "3":    #SHOW ALL ON LOAN
        print(f"{'TITLE':33} {'ON LOAN'}")
        print("---------------------------------------------")
        for i in range(len(loan)):
            print(f"{title[i]:33} {loan[i]}")
        print("---------------------------------------------")
        input("\nPress any key to continue...")
       
    elif search_type == "4":    #TITLE SEARCH
        print(f"\nYou have chosen to search by TITLE")

        search = input("\nWhat TITLE would you like to search for: ")
        #SEQUENTIAL SEARCH FOR MULTIPLE VALUES MATCHING SEARCH TERM
        for i in range(len(title)):
            if search.lower() in title[i].lower():
                found.append(i)

        #Display results
        if not found: 
            print(f"Sorry, your search for {search} came up empty :[")
        else:
            display("x", len(found))
        input("\nPress any key to continue...")

    elif search_type == "5":    #AUTHOR SEARCH
        print(f"\nYou have chosen to search by AUTHOR")

        search = input("\nWhat AUTHOR would you like to search for: ")
        #SEQUENTIAL SEARCH FOR MULTIPLE VALUES MATCHING SEARCH TERM
        for i in range(len(author)):
            if search.lower() in author[i].lower():
                found.append(i)

        #Display results
        if not found: 
            print(f"Sorry, your search for {search} came up empty :[")
        else:
            display("x", len(found))
        input("\nPress any key to continue...")
    

    elif search_type == "6":    #GENRE SEARCH
        print(f"\nYou have chosen to search by GENRE")

        search = input("\nWhat GENRE would you like to search for: ")
        #SEQUENTIAL SEARCH FOR MULTIPLE VALUES MATCHING SEARCH TERM
        for i in range(len(genre)):
            if search.lower() in genre[i].lower():
                found.append(i)
        
        #Display results
        if not found:
            print(f"Sorry, your search for {search} came up empty :[")
        else:
            display("x", len(found))
        input("\nPress any key to continue...")


    elif search_type == "7":       #LIBRARY # SEARCH
        print(f"\nYou have chosen to search by LIBRARY #")


        #allow the user to search for ONE specific and unique name value (binary search!)
        search = input("\nEnter the # you are looking for: ")
        #BUBBLE SORT:
        for i in range(0, len(libNum) - 1):
            for j in range(0, len(libNum) - 1):
                if libNum[j] > libNum[j + 1]:
                    swap(j, libNum)
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pCount)
                    swap(j, status)

        #BINARY SEARCH:
        min = 0                             #Lowest possible index
        max = len(libNum) - 1                 #Highest index
        mid = int((min + max) / 2)          #Middle index in sorted list

        while min < max and search.lower() != libNum[mid].lower():
            if search.lower() < libNum[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)

        if search.lower() == libNum[mid].lower():
            print(f"Your search for {search} was found, see details below:")
            display(mid, len(libNum))
        else:
            print(f"Sorry, we could not find your search for {search}. Please try again.")
        input("\nPress any key to continue...")


    elif search_type == "8":    #EXIT
        print(f"\nYou have chosen to EXIT")
        ans = "N"

#final print statement
print("\nThank you for using my program, goodbye!\n")