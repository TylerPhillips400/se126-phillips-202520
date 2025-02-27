#W8D2 - Dictionary Review + Gaining Data from Text Files
#This demo utilizes: dictionary_file.csv

#---IMPORTS-----------------------------------------------------
import csv
#---MAIN EXECUTING CODE-----------------------------------------
library = {
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince",
}

#--connected to file------------------------------------------
with open("week8/dictionary_file.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #For every record in the file, do the following
        #File --> 2D list; rec --> 1 record's data, also list!
        library.update({rec[0] : rec[1]})
        #library_num --> rec[0], a string
        #tile --> rec[1], also a string

#--disconnected from file---------------------------------------

print(f"{'KEY':4} : {'TITLE'}")
print("-" * 50)
for key in library:
    #For every key found in the library dictionary
    print(f"{key.upper():4} : {library[key]}")
print("-" * 50)

#--SEQUENTIAL SEARCH with DICTIONARIES--------------------------
'''
search = input("\nEnter the TITLE you are looking for: ")

found = []

for key in library:
    if search.lower() in library[key].lower():
        found.append(key)
    
if found != 0:
    print(f"We found your search for {search}, here is the info: \n")
    print(f"{'KEY':4} : {'TITLE'}")
    print("-" * 50)
    for i in range(len(found)):
        print(f"{found[i].upper():4} : {library[found[i]]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[")
'''

search = input("\nEnter the LIBRARY NUM you are looking for: ")

found = 0

for key in library:
    if search.lower() == key.lower():
        found = key
    
if found != 0:
    print(f"We found your search for {search}, here is the info: \n")
    print(f"{'KEY':4} : {'TITLE'}")
    print("-" * 50)
    print(f"{found.upper():4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[")