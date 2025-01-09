#Tyler Phillips
#SE126.04
#W1D2 Lab Demo: SE116 Review
#1-9-2025 [W1D2]

#PROGRAM PROMPT: This is a temperature conversion program, it allows a user to enter as many Fahrenheit temps as they'd like and then shows the Celsius conversoion for each. It also counts the number of temps and determines the average of all temps entered. 

#VARIABLE DICTIONARY
#temp_count     the total number of all temps entered
#temp_total     the sum total of all temps entered
#avg_temp       the avg temp entered (avg_temp = temp_total / temp_count)
#tempF          the temp in Fahrenheit, entered by the user
#tempC          the temp in Celsius (tempC = (tempF - 32) * (5 / 9))
#answer         loop control; value determines if loop repeats, entered by the user

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
def again():    #<--Function header
    '''This function asks a user if they'd like to enter annother temp, checks tge response for validity, and then returns a valid response back to the main program'''

    ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    #User error trap loop - ensures user provides valid value
    while ans != "y" and ans != "n":
        print("***INVALID ENTRY!***")
        ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    return ans      #This value will replave the function call in the main code

def converter(f):
    #'f' is a parameter
    '''This function is passsed an argument value of 'f' (a tempF), converts to tempC, and then returns the conversion value'''
    c = (f - 32) * (5 / 9)

    return c

#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
temp_count = 0
temp_total = 0

answer = "y"       #Loop Control Variable

#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y":

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    #necessary calculations
    tempC = converter(tempF)

    #math processes needed later for average calculation
    temp_count = temp_count + 1     #SHORT VERSION ----->  temp_count += 1
    temp_total += tempF

    #display data to user
    print(f"\n\t\tTEMP# {temp_count}\tTEMP {tempF:.1f}F = TEMP {tempC:.1f}C\n")

    #loop control! allowing a way back in or out of the loop based on the value of answer
    answer = again()        #Return value will replace this function call and store to 'answer'

#out of loop

#average calculation and conversion
avg_tempF = temp_total / temp_count 

avg_tempC = converter(avg_tempF)


#final displays
print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVGERAGE TEMP {0:.1f}F  |  {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThank you for using the program. Goodbye.\n\n")



