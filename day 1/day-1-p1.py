#!/usr/bin/env python

f = open("day-1-input.txt", "r")
string = f.read()
f.close()
calibration = string.split('\n')

def getFirstNumber(string):
    for i, x in enumerate(string):
        if x.isdigit():
            return(x)

num = 0
# Loop through calibration lines
for cal in calibration:
    # Get first number in string
    x = getFirstNumber(cal)
    # Get last number in string
    y = getFirstNumber(cal[::-1])
    # Concatenate and numerify
    num += int(x + y)

print(num)
