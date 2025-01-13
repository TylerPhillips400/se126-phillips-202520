#Tyler Phillips
#SE126.04
#Lab 1
#1-10-2025

#PROGRAM PROMPT: You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. Th program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#VARIABLE DICTIONARY
#people             The amount of people attending that will be passed through the difference function
#max_cap            The maximum capacity of the room that will be passed through the difference functiom
#dif                The difference of the max capacity and the amount of people attending
#response           The response of the user that is passed through the decision function
#answer             When the user inputs "y" the program will run again through the while loop
#meeting_name       The name of the meeting [input]
#room_cap           The rooms max capacity [input]
#ppl_attend         The amoount of people attending the meeting [input]
#diff               the difference of the max capacity and people attending 
#ppl                The absolute value of diff for when the diff is negative

#--------IMPORTS----------------------------------------------
#Import os for clear() function
from os import name, system
#--------FUNCTIONS--------------------------------------------
def clear():    #<--FUNCTION HEADER
    if name == 'nt':        #windows os
        _ = system('cls')
    else:                   #linux or mac
        _ = system('clear')

def difference(people, max_cap):
    #necessary calculations
    dif = max_cap - people

    return dif

def decision(response):  
    #Error Trap loop
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("\nDo you have a different amount of poeple to enter? [y/n]: ").lower()

    return response

#--------MAIN EXECUTING CODE----------------------------------

clear()     #Clear Terminal

print("\nWelcome to the Meeting Room Capacity Program\n")

answer = "y"        #Loop Control Variabe

while answer == "y":

    #Asking user for data
    meeting_name = input("\nEnter the name of the meeting: ")
    room_cap = int(input("\nHow many people can be in the room at once?: "))
    ppl_attend = int(input(f"\nHow many people are planning on attending {meeting_name}?: "))

    #Malipulation of Data
    diff = difference(ppl_attend, room_cap)

    #If/Elif/Else statements for outcome of difference()
    if room_cap > ppl_attend:
        print(f"\nThe meeting meets fire saftey requirements and you can add {diff} more people")
    elif room_cap < ppl_attend:
        ppl = abs(diff)     #Absolute value conversion
        print(f"\nThe meeting does not meets fire saftey requirements and you need to remove {ppl} people")
    else:
        print(f"\nThe meeting meets fire saftey requirements and you can not add anyone else")

    #Loop Control
    answer = input("\nDo you have a different amount of poeple to enter? [y/n]: ").lower()
    answer = decision(answer)


#Final Display
print("\n\n Thank you for using the program. Goodbye!")
