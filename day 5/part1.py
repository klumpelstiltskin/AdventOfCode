#!/usr/bin/env python

f = open("input.txt", "r")
string = f.read()
f.close()
sections = string.split('\n\n')

seed_list = []
seed_to_location_map = []

for i, section in enumerate(sections):
    # Seed list
    if i==0:
        seed_list = [int(x) for x in section.split(' ')[1:]]
    else:
        x = section.split('\n')
        key = x[0][:-5]
        val = []
        for item in x[1:]:
            val.append([int(x) for x in item.split(' ')])
        seed_to_location_map.append(val)

def getOutputItemFromMap(map_, input_item):
    for line in map_:
        source = line[1]
        dest = line[0]
        ran = line[2] - 1
        # Check if input is within map
        if source <= input_item <= source + ran:
            return(dest + (input_item - source))
    return(input_item)

lowest_location = 0

# Loop through all seeds
for i, seed in enumerate(seed_list):
    val = seed
    # Loop through all maps to get location of seed
    for map_ in seed_to_location_map:
        val = getOutputItemFromMap(map_, val)

    if val < lowest_location or i == 0:
        lowest_location = val

print(lowest_location)