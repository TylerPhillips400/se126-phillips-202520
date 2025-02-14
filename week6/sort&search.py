#W6D2 - Bubble Sorting & Binary Search Review

#https://www.google.com/search?q=bubble+sort+visualization&rlz=1C1GCHA_enUS1119US1119&oq=bubble+sort+visualization&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIICAQQABgWGB4yCAgFEAAYFhgeMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoFMg0ICBAAGIYDGIAEGIoF0gEIMzUwMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:7e94f359,vid:0BkoXZBbhfU,st:0 

#***IMPORTANT: 
#   In order to use binary search, 2 caveats must be fulfilled:
#      *the list we intend to search through is ORDERED
#      *the list we intend to search through is populated with UNIQUE VALUES (no repeats!)

#----IMPORTS-------------------------------------------------
import csv

#----FUNCTIONS-----------------------------------------------
def display(x, foundList, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an index and we have one value, otherwise we have multiple

            records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'CLASS':8}  {'NAME':10}  {'MEANING':25}  {'CULTURE'}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{class_type[x]:8}  {name[x]:10}  {meaning[x]:25}  {culture[x]}")

    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{class_type[foundList[i]]:8}  {name[foundList[i]]:10}  {meaning[foundList[i]]:25}  {culture[foundList[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{class_type[i]:8}  {name[i]:10}  {meaning[i]:25}  {culture[i]}")

    print("----------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#----MAIN CODE-----------------------------------------------
practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

class_type = [] #rec[0] in file; repeats --> SEQUENTIAL
name = []       #rec[1] in file; unique  --> BINARY
meaning = []    #rec[2] in file; unique  --> BINARY
culture = []    #rec[3] in file; repeats --> SEQUENTIAL

with open("week6/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#disconnected from file------------------------------------

#display whole list data to user
display("x",0,len(class_type)) #practice with function

ans = input("Would you like to enter the search program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()

#main searching loop
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE") #shows all of either elf or dragon
    print("2. Search by NAME") #binary search review
    print("3. Search by MEANING") #find part of a whole
    print("4. EXIT")

    search_type = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4"]:
         print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":
        print(f"\nYou have chosen to search by TYPE")

        search = input("Which type: 'dragon' or 'elf':").lower()

        if search not in ["dragon", "elf"]: 
            #could also be: if search.title() not in class_type:
            print("***INVALID ENTRY!***\nPlease try again")

        else:
            found = []
            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search for {search} could not be completed :[")
            else:
                print(f"Your search for {search} is complete! Details below:")
                display("x", found, len(found))

    elif search_type == "2":
        print(f"\nYou have chosen to search by NAME")

        #BINARY SEARCH: 
        #               * requires a collection of UNIQUE values to search through
        #               * requires the collection to be SORTED (ORDERED)
        #                       ascending or descending ; alpha or numeric


        #ALWAYS SORT BEFORE YOU SEARCH when using BINARY SEARCH!

        #BUBBLE SORT ALGORITHM -- copythis from the code in Canvas! 
        for i in range(0, len(name) - 1):#outter loop

            for index in range(0, len(name) - 1):#inner loop
                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(name[index] > name[index + 1]):
                    #if above is true, swap places!
                    swap(index, name)

                    #swap all other values
                    swap(index, class_type)
                    swap(index, meaning)
                    swap(index, culture)
        
        #check your sorting!
        display("x", 0, len(name))

        #BINARY SEARCH
        search = input("Enter the NAME you are looking for: ")

        min = 0 
        max = len(name) - 1
        mid = int((min + max) / 2)

        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid - 1
            else:
                #search > name[mid]
                min = mid + 1
            
            mid = int((min + max) / 2)  

        if search == name[mid]:
            display(mid, 0, len(name))  
        else:
            print(f"Your search for {search} came up empty :[")

    elif search_type == "3":
        print(f"\nYou have chosen to search by MEANING")

        search = input("Which name meaning are you looking for:").lower()

        found = []

        #allow the program to search for parts of a name like 'dragon' or 'light'
        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found: 
            print(f"Sorry, we have no names related to the meaning you entered: '{search}'")
        else:
            display("x", found, len(found))

    elif search_type == "4":
        print(f"\nYou have chosen to EXIT")
        ans = "N"