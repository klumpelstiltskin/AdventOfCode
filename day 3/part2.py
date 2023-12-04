#!/usr/bin/env python

f = open("input.txt", "r")
string = f.read()
f.close()
lines = string.split('\n')

# Loop through each line to get number list
num_list = []
symbol_list = []
for l, line in enumerate(lines):
    prev_char = '.'
    num_string = ''
    found_index = 0
    for i, char in enumerate(line):
        if char.isdigit():
            num_string += char
            if not prev_char.isdigit():
                # New number
                found_index = i
            # corner case for number at end of string
            if i==len(line) -1:
                # found number
                num_list.append((found_index, l, num_string))
        elif prev_char.isdigit():
            # found number
            num_list.append((found_index, l, num_string))
            num_string = ''
        if not char.isdigit() and char != ".":
            symbol_list.append([[i, l], char])
        prev_char = char

gear_list = []
def isAdjacentToSymbol(num):
    x = num[0]
    y = num[1]
    length = len(num[2])
    perimeter = []
    flag = False
    # print(num)
    # Top side
    for i in range(length + 2):
        perimeter.append([(x - 1 + i), y + 1])
    # Bottom side
    for i in range(length + 2):
        perimeter.append([(x - 1 + i), y - 1])
    # Left side
    perimeter.append([(x - 1), y])
    # Right side
    perimeter.append([(x + length), y])
    # Cull all outside border

    perimeter[:] = [pos for pos in perimeter if (pos[0]>=0 and pos[1]>=0)]
    # Check if match between perimeter and symbol

    for pos in perimeter:
        for symbol in symbol_list:
            if(symbol[0]==pos):
                # Found adjacent symbol. Add to gear list (pt2)
                if(symbol[1]=='*'):
                    gear_list.append([pos, num[2]])
                flag = True
    return(flag)

sum_total = 0
for num in num_list:
    if isAdjacentToSymbol(num):
        continue

for i in range(0, len(gear_list)):
    for j in range(i+1, len(gear_list)):
        if(gear_list[i][0] == gear_list[j][0]):
            sum_total += int(gear_list[i][1]) * int(gear_list[j][1])

print(sum_total)






