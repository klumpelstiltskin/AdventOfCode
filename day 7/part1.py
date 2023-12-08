#!/usr/bin/env python

import math
from collections import defaultdict

CARD_STRENGTHS = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                  '7', '6', '5', '4', '3', '2']

HAND_TYPES = ['FIVE  OF A KIND',
              'FOUR OF A KIND',
              'FULL HOUSE',
              'THREE OF A KIND',
              'TWO PAIR',
              'ONE PAIR',
              'HIGH CARD']

f = open("input.txt", "r")
string = f.read()
f.close()
lines = string.split('\n')

def isFiveOfAKind(hand):
    return(True if len(set(hand)) == 1 else False)

def isFourOfAKind(hand):
    card_counts = defaultdict(lambda:0)
    for card in hand:
        card_counts[card] += 1
    if sorted(card_counts.values()) == [1, 4]:
        return(True)
    return(False)

def isFullHouse(hand):
    card_counts = defaultdict(lambda:0)
    for card in hand:
        card_counts[card] += 1
    if sorted(card_counts.values()) == [2, 3]:
        return(True)
    return(False)

def isThreeOfAKind(hand):
    card_counts = defaultdict(lambda:0)
    for card in hand:
        card_counts[card] += 1
    x = set(card_counts.values())
    if set(card_counts.values()) == {1, 3}:
        return(True)
    return(False)

def isTwoPair(hand):
    card_counts = defaultdict(lambda:0)
    for card in hand:
        card_counts[card] += 1
    if sorted(card_counts.values()) == [1, 2, 2]:
        return(True)
    return(False)

def isOnePair(hand):
    card_counts = defaultdict(lambda:0)
    for card in hand:
        card_counts[card] += 1
    if sorted(card_counts.values()) == [1, 1, 1, 2]:
        return(True)
    return(False)

def rankHand(hand):
    if isFiveOfAKind(hand):
        return(7)
    elif isFourOfAKind(hand):
        return(6)
    elif isFullHouse(hand):
        return(5)
    elif isThreeOfAKind(hand):
        return(4)
    elif isTwoPair(hand):
        return(3)
    elif isOnePair(hand):
        return(2)
    # high card
    return(1)

hands = []
# First rank hands based on strength
for line in lines:
    x = line.split(' ')
    rank = rankHand(x[0])
    hands.append({'hand':x[0], 'bid':x[1], 'rank': rank})

strength = 1
for i in range(1, len(HAND_TYPES) + 1):
    x = [hand for hand in hands if hand['rank']==i]
    if(x):
        newlist = sorted(x, key=lambda d: d['hand'])
            # rank best hand in same type
        print(strength, newlist)
        strength += 1

# for hand in hands:
#     print(hand)
