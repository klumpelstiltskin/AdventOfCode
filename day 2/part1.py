#!/usr/bin/env python

MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}

def isGameSetValid(game_set):
    for game in game_set:
        for key in game:
            if game[key] > MAX_CUBES[key]:
                return(False)
    return(True)

f = open("input.txt", "r")
string = f.read()
f.close()
game_set_list = string.split('\n')

sum_of_valid_ids = 0

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
    
    if isGameSetValid(b):
        # print(b, i)
        sum_of_valid_ids += i

print(sum_of_valid_ids)