#W2D1 - Text File Handling Intro Demo

#STEP 1: import the CSV (comma separated value) library
import csv

total_records = 0       #Holds total number of records in the file

#STEP 2: connect to the file

#--connected to file------------------------------------------
#include reative file path in open() 
#Make sure \ switches to / in the file path
with open("week2/simple.csv") as csvfile:
    #make sure to indent inside of code block

    #allow the csv.reader() to access and read the file path; stores contentsto 'file' [a 2D list / matrix / table]
    file = csv.reader(csvfile)

    #print for headers
    print(f"\t{'NAME':10}\t{'NUM':3}\t{'COLOR'}")
    print("-----------------------------------------")
    #STEP 3: process through every record (row) in the file
    for record in file:
        #add +1 to total_records to keep accurate count of records
        total_records += 1

        #print(record) #entire record / row data as a list
        name = record[0]
        number = record[1]
        color = record[2]

        print(f"\t{name:10}\t{number:3}\t{color.title()}")
        #.title() set the word as a title - First letter becomes capital




#--disconnected to file---------------------------------------
print("-----------------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")