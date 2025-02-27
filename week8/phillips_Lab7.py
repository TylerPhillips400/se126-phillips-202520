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

ans = input("\nWould you like to enter the dictionary program? [y/n]: ").lower()

#Error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the dictionary program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    print("\tDICTIONARY MENU")
    print("1. Show All Words")      
    print("2. Search for a word")     
    print("3. Add a Word")  
    print("4. EXIT") 

    search_type = input("\nHow would you like to do in the menu? [1-4]: ")

    if search_type not in ["1", "2", "3", "4"]:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":    #SHOW ALL WORDS
        #Display of all words and definitions in csvfile
        print(f"{'WORD':13} : {'DEFINITION'}")
        print("-" * 180)
        for key in dictionary:
            #For every key found in the library dictionary
            print(f"{key:13} : {dictionary[key]}")
        print("-" * 180)
    
    elif search_type == "2":
        search = input("\nEnter the WORD you are looking for: ")
        found = 0

        for key in dictionary:
            if search.lower() == key.lower():
                found = key
            
        if found != 0:
            print(f"We found your search for {search}, here is the info: \n")
            print(f"{'WORD':13} : {'DEFINITION'}")
            print("-" * 180)
            print(f"{found.lower():13} : {dictionary[found]}")
            print("-" * 180)
        else:
            print(f"We could not find your search for {search} in the dictionary, sorry")

    elif search_type == "3":

        new_word = input("\nWhat is the word that you would like to add to the dictionary?: ")
        new_def = input(f"What is the definition if {new_word}?: ")
        dictionary[new_word] = new_def
        
        words.append(new_word)
        definition.append(new_def)

        #WRITING NEW DATA
        file = open("week8/updated_words.csv", "w")

        for i in range(len(words)):
            if i in range(0, 24):
                file.write(f"{words[i]},{definition[i]}\n")
            elif i in range(25):   #So that there is no extra line created in the CSV file
                file.write(f"{words[i]},{definition[i]}")
            else:
                file.write(f"{words[i]},{definition[i]}")
        file.close()    #Closing new file created

        #Print statement for processing word and putting them into a new file
        print(f"\n{len(dictionary)} records processed and made into the new updated_words.csv file\n")

    elif search_type == "4":    #EXIT
        print(f"\nYou have chosen to EXIT")
        ans = "N"

#final print statement
print("\nThank you for using my program, goodbye!\n")