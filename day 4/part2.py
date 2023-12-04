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
    index = [int(x) for x in l[0].split(' ') if x.isdigit()]
    scratchcard_list.append({'index': index, 'num_cards': 1, 'my_nums': my_nums, 'winning_nums': winning_nums})

# Fill new scratchlist with extras
for i, card in enumerate(scratchcard_list):
    print(i)
    for c in range(card['num_cards']):
        matches = 0
        # Determine number of points
        for a in card['my_nums']:
            for b in card['winning_nums']:
                if a == b:
                    matches += 1
        # Now add new entries given the points awarded
        
        for j in range(1, matches + 1):
            scratchcard_list[i+j]['num_cards'] +=1

sum_total = 0
for card in scratchcard_list:
    sum_total += card['num_cards']

print(sum_total)