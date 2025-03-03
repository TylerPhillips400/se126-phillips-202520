#Tyler Phillips
#SE126.04
#Lab 5
#2-27-2025

#PROMPT: Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary.

#VARIABLE DICTIONARY:
#csvfile            Storing the relative path from the CSV file
#file               Passing the CSV file to the reader method
#rec                Processing all records in the CSV file
#i                  Index of each field of data from all records
#j                  Placeholder for index swaping for alphabetical order
#listname           list name for the swap() to bubble sort
#temp               temp variable for bubble sort swap()
#words              All words from the CSV file appened into a list
#definition         All definitions from the CSV file appened into a list
#dictionary         Dictionary updated by using the first record : 2nd record
#ans                Askes user if they would like to enter the dictionary program and allows the program to loop [input]
#search_type        Askes user what they would like to do in the search menu [input]
#key                Key is the firt record or word that correlates to the definition
#found              Variable containing the found item for displaying a word that is searched for
#new_word           Askes user what new word they would like to add [input]
#new_def            Askes user what the definition of the new word they added was [input]

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

def swap(i, listName):  #Swaping for descending or ascending order
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#-Main Code-----------------------------------------------------------------------------------

clear()     #Clear Terminal

#Empty lists
words = []
definition = []

#Dictionary
dictionary = {}

#--connected to file------------------------------------------
with open("week8/words.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        words.append(rec[0])
        definition.append(rec[1])
        dictionary.update({rec[0] : rec[1]})

#--disconnected from file---------------------------------------
#Asks user if they would like to enter the program
ans = input("\nWould you like to enter the dictionary program? [y/n]: ").lower()

#Error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the dictionary program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    print("\tDICTIONARY MENU")                                  #Search menu
    print("1. Show All Words")                                  #Show all
    print("2. Search for a word")                               #Search for specific word
    print("3. Add a Word")                                      #Add word
    print("3.5. Show All Words Sorted in Alphabetial Order")    #Show all in alphabetical order
    print("4. EXIT")                                            #EXIT

    search_type = input("\nHow would you like to do in the menu? [1-4]: ")

    if search_type not in ["1", "2", "3", "3.5", "4"]:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":    #SHOW ALL WORDS
        #Display of all words and definitions in csvfile
        print(f"{'WORD':13} : {'DEFINITION'}")
        print("-" * 180)
        for key in dictionary:
            #For every key found in the library dictionary
            print(f"{key:13} : {dictionary[key]}")
        print("-" * 180)
    
    elif search_type == "2":        #WORD SEARCH
        search = input("\nEnter the WORD you are looking for: ")
        found = 0

        for key in dictionary:
            if search.lower() == key.lower():
                found = key
            
        if found != 0:
            #Found display
            print(f"We found your search for {search}, here is the info: \n")
            print(f"{'WORD':13} : {'DEFINITION'}")
            print("-" * 180)
            print(f"{found.lower():13} : {dictionary[found]}")
            print("-" * 180)
        else:   #not found
            print(f"We could not find your search for {search} in the dictionary, sorry")

    elif search_type == "3":        #ADD NEW WORD TO DICTIONARY
        #Asking for new data
        new_word = input("\nWhat is the word that you would like to add to the dictionary?: ")
        new_def = input(f"What is the definition if {new_word}?: ")
        dictionary[new_word] = new_def  #Adding data to the dictionary
        
        #Appending new word and definition to the list for new file
        words.append(new_word)
        definition.append(new_def)

        #WRITING NEW DATA
        file = open("week8/updated_words.csv", "w")

        for i in range(len(words)):
            if i in range(len(words) - 1):
                file.write(f"{words[i]},{definition[i]}\n")
            else:   #So that there is no extra line created in the CSV file
                file.write(f"{words[i]},{definition[i]}")
        file.close()    #Closing new file created

        #Print statement for processing word and putting them into a new file
        print(f"\n{len(dictionary)} records processed and made into the new updated_words.csv file\n")

    elif search_type == "3.5":  #Sorted words in alphabetical order
        #BUBBLE SORT: ALPHABETICAL SORTING
        for i in range(0, len(words) - 1):
            for j in range(0, len(words) - 1):
                if words[j] > words[j + 1]:
                    swap(j, words)
                    swap(j, definition)

        #DISPLAY
        print(f"{'WORD':13} : {'DEFINITION'}")
        print("-" * 180)
        for i in range(len(words)):
            print(f"{words[i]:13} : {definition[i]}")
        print("-" * 180)


    elif search_type == "4":    #EXIT
        print(f"\nYou have chosen to EXIT")
        ans = "N"

#final print statement
print("\nThank you for using my program, goodbye!\n")