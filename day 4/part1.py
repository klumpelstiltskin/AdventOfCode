#!/usr/bin/env python

f = open("input.txt", "r")
string = f.read()
f.close()
lines = string.split('\n')

scratchcard_list = []
for line in lines:
    l = line.split(':')
    card = l[1].split('|')
    winning_nums = [int(x) for x in card[0].split(' ') if x.isdigit()]
    my_nums = [int(x) for x in card[1].split(' ') if x.isdigit()]
    scratchcard_list.append({'my_nums': my_nums, 'winning_nums': winning_nums})


# 
# for i, card in enumerate(scratchcard_list):
#     points = 0
#     for a in card['my_nums']:
#         for b in card['winning_nums']:
#             if a == b:
#                 if points==0:
#                     points = 1
#                 else:
#                     points *= 2
#     sum_total += points

sum_total = 0
for i, card in enumerate(scratchcard_list):
    points = 0
    for a in card['my_nums']:
        for b in card['winning_nums']:
            if a == b:
                if points==0:
                    points = 1
                else:
                    points *= 2
    sum_total += points

print(sum_total)