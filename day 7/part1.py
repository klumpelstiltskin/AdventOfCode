#!/usr/bin/env python

import math
from collections import defaultdict

CARD_STRENGTHS = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                  '7', '6', '5', '4', '3', '2']

HAND_TYPES = ['HIGH CARD',
              'ONE PAIR',
              'TWO PAIR',
              'THREE OF A KIND',
              'FULL HOUSE',
              'FOUR OF A KIND',
              'FIVE  OF A KIND']

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
        return(HAND_TYPES[6])
    elif isFourOfAKind(hand):
        return(HAND_TYPES[5])
    elif isFullHouse(hand):
        return(HAND_TYPES[4])
    elif isThreeOfAKind(hand):
        return(HAND_TYPES[3])
    elif isTwoPair(hand):
        return(HAND_TYPES[2])
    elif isOnePair(hand):
        return(HAND_TYPES[1])
    # high card
    return(HAND_TYPES[0])

hands = []
# First group hands based on strength
for line in lines:
    x = line.split(' ')
    rank = rankHand(x[0])
    hands.append({'hand':x[0], 'bid':x[1], 'rank': rank})

rank = 1
total_winnings = 0
for i in HAND_TYPES:
    same_hand_types = [hand for hand in hands if hand['rank']==i]
    # Check if empty string
    if(same_hand_types):
        # Sort each hand by highest strength in each hand type
        res = sorted([h for h in same_hand_types], key=lambda word: [CARD_STRENGTHS[::-1].index(c) for c in word['hand']])
        for j in res:
            total_winnings += int(j['bid']) * rank
            rank += 1

print(total_winnings)
