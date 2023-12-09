#!/usr/bin/env python

import math
from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
f.close()

def computeDiffListArray(values):
    diff_list = values
    diff_list_array = [values]

    while not all(v == 0 for v in diff_list):
        diff_list = computeDiffList(diff_list)
        diff_list_array.append(diff_list)

    return(diff_list_array)

def computeDiffList(values):
    diff_list = []
    for i in range(len(values) - 1):
        diff_list.append(values[i + 1] - values[i])
    return(diff_list)

total = 0
for line in lines:
    values = line.rstrip().split(' ')
    values = [int(x) for x in values]

    # Compute difference
    diff_list_array = computeDiffListArray(values)

    # Now compute reverse prediction from lists
    for i in range(len(diff_list_array) - 1, 0, -1):
        pred = diff_list_array[i - 1][0] - diff_list_array[i][0]
        diff_list_array[i - 1].insert(0, pred)
    total += pred

print(total)