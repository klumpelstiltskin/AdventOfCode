#!/usr/bin/env python

num_table = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

f = open("day-1-input.txt", "r")
string = f.read()
f.close()
calibration = string.split('\n')

def isSpelledNumber(string, table):
    val = 0
    # Loop through list to check for match.
    # Only match if found index is 0
    for i, num in enumerate(table):
        index = string.find(num)
        if index == 0:
            # print("match found ", i+1)
            val = str(i + 1)
            break
    return(val)

def getFirstNumber(string, table):
    for i, x in enumerate(string):
        # First check if it's a numeric digit
        if x.isdigit():
            return(x)
        # Next check if it's a spelled number
        else:
            val = isSpelledNumber(string[i:], table)
            if val != 0:
                return(val)

total = 0
# Loop through calibration lines
for cal in calibration:

    # Get first number in string
    x = getFirstNumber(cal, num_table)

    # Reverse string and table to get last number
    y = getFirstNumber(cal[::-1], [i[::-1] for i in num_table])

    # Concatenate and numerify
    num = int(x + y)
    print(num)
    total += num

print(total)
