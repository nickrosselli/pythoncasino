# helpers.py
import json

# Open JSON file
f = open("./config.json")

# Return JSON data as a dictionary
conf = json.load(f)

# Close JSON file
f.close()


# Functions
#-----------#
# inputted data
def getString(prompt):
    value = ""
    while value == "":
        value = input(prompt)
        if len(value) == 0:
            print(conf['emptyEntry'])
    return value

def getInt(prompt):
    valid = False
    value = ""
    while valid == False:
        try:
            value = int(getString(prompt))
            valid = True
        except ValueError:
            print(conf['invalidInt'])
    return value

def getFloat(prompt):
    valid = False
    value = ""
    while valid == False:
        try:
            value = float(getString(prompt))
            valid = True
        except ValueError:
            print(conf['invalidFloat'])
    return value

# testing
# if __name__=="__main__":
#     val=getString("Enter a string: ")
#     print(f"{type(val)} is: {val}")