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


# Find starting nodes
next_nodes = [key for key,val in node_map.items() if key[2] == 'A']

next_node = next_nodes[0]

count = 0
check = [True if n[2]=='Z' else False for n in next_nodes]
while not all(check):
    for i in instructions:
        count += 1
        for j, node in enumerate(next_nodes):
            # for next_node in next_nodes:
            next_nodes[j] = findNextNode(node_map, node, i)
        # print(next_nodes)
        check = [True if n[2]=='Z' else False for n in next_nodes]
        if all(check):
            break
    if count%1000 == 0:
        print(count)

print(count)