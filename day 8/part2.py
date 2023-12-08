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
    left = ''.join([x for x in string[2] if x.isalnum()])
    right = ''.join([x for x in string[3] if x.isalnum()])
    node_map[string[0]] = [left, right]

def findNextNode(node_map, node, direction):
    nn = 0
    if(direction=='L'):
        nn = node_map[node][0]
    else:
        nn = node_map[node][1]
    return(nn)

def traverseUntilToken(_map, _instructions, _start_node):
    next_node = _start_node
    count = 0
    while next_node[2]!='Z':
        for i in _instructions:
            count += 1
            next_node = findNextNode(node_map, next_node, i)
            if next_node[2]=='Z':
                return(count)

# Find starting nodes
next_nodes = [key for key,val in node_map.items() if key[2] == 'A']

tokenCounts = []
for j, node in enumerate(next_nodes):
    tokenCounts.append(traverseUntilToken(node_map, instructions, node))
print(math.lcm(*tokenCounts))
