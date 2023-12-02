#!/usr/bin/env python

def findCubePower(game_set):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}

    # First find minimum set of cubes
    for game in game_set:
        for key in game:
            min_cubes[key] = game[key] if game[key]>min_cubes[key] else min_cubes[key]

    # Now calculate power
    pow = 1
    for key in min_cubes:
        pow *= min_cubes[key]
    return(pow)

f = open("input.txt", "r")
string = f.read()
f.close()
game_set_list = string.split('\n')

sum_of_powers = 0

# Loop through each game set
for i, gs in enumerate(game_set_list, 1):
    index = gs.find(':')
    game_set = gs[index+2:].split(';')
    # Loop through each game to create dictionary
    b = []
    for game in game_set:
        x = game.split(',')
        a = {}
        for y in x:
            z = y.strip(' ').split(' ')
            a[z[1]] = int(z[0])
        b.append(a)

    sum_of_powers += findCubePower(b)

print(sum_of_powers)