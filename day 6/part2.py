#!/usr/bin/env python

import math

f = open("input.txt", "r")
string = f.read()
f.close()
lines = string.split('\n')

max_time = int(lines[0].split(':')[1].replace(" ", ""))
max_dist = int(lines[1].split(':')[1].replace(" ", ""))

winning_ways = 0

ways = 0
for hold_time in range(1, max_time):
    race_dist = (max_time - hold_time)*hold_time
    if race_dist > max_dist:
        winning_ways += 1

print(winning_ways)