#!/usr/bin/env python

import math
from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
f.close()

instructions = lines[0].strip()

node_map = defaultdict(lambda:0)
for x in lines[2:]:
    string = x.split(' ')
    left = ''.join([x for x in string[2] if x.isalpha()])
    right = ''.join([x for x in string[3] if x.isalpha()])
    node_map[string[0]] = [left, right]

def findNextNode(node_map, node, direction):
    nn = 0
    if(direction=='L'):
        nn = node_map[node][0]
        print('next node is ', node_map[node][0])
    else:
        nn = node_map[node][1]
        print('next node is ', node_map[node][1])
    return(nn)

next_node = 'AAA'
count = 0
while next_node!='ZZZ':
    for i in instructions:
        count += 1
        next_node = findNextNode(node_map, next_node, i)
        if next_node=='ZZZ':
            break

print(next_node, count)
