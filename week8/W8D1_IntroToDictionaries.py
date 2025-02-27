#W8D1 - Introduction to Dictionaries

#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 

#---IMPORTS-----------------------------------------------------

#---MAIN EXECUTING CODE-----------------------------------------

#start by creating a populated dictionary 
myCar = {
    #'key' : value, 
    "make": "Ford",
    "model": "SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    #keys cannot be repeated/NO DUPLICATES allowed
    #repeats will replace first value,see 'color' key below in print
    "color" : "red"
}

#display the entire dictionary -> 'myCar'
print(myCar)

#display just the 'make' and 'model' values of the dictionary 'myCar'

#dictionaryName["keyName"] --> accesses stored value
#"keyName" will always be a STRING index, created by developer
print(f"My car is a {myCar["make"]} {myCar["model"]}")

#keys cannot be repeated WITHIN a dictionary, but they can be reused across unique dictionary names: myCar vs yourCar
yourCar = {
    #'key' : value, 
    "make": "GMC",
    "model": "Canyon",
    "year": 2019,
    "name": "Jolly",
    "color": "black",
    "friends": ["Ray", "Matt", "Duncan"]
}

print(f"Rob's car is a {yourCar["make"]} {yourCar["model"]}")

#since "friends" gives access to a list, secondary [] are used to point to which value in said list
print(f"{yourCar["friends"][2]}")

#processing through a dictionary and its keys
for key in myCar:
    print(f"{key.upper()} : {myCar[key]}")

#add a key and value to a pre-existing dictionary
yourCar["plate"] = "12345"