#!/usr/bin/env python

import math

f = open("input.txt", "r")
string = f.read()
f.close()
lines = string.split('\n')

time = [int(x) for x in lines[0].split(' ') if x.isdigit()]
distance = [int(x) for x in lines[1].split(' ') if x.isdigit()]
races = zip(*[time, distance])

winning_prod = 1
winning_ways = []
for race in races:
    max_time = race[0]
    max_dist = race[1]
    ways = 0
    for hold_time in range(1, max_time):
        race_dist = (max_time - hold_time)*hold_time
        if race_dist > max_dist:
            ways += 1
    winning_ways.append(ways)

print(math.prod(winning_ways))