#!/usr/bin/env python
"""
Advent of Code 2017 - Day 5 (http://adventofcode.com/2017/day/5)
"""

with open('data/day5.txt') as openfile:
    path = [int(x) for x in openfile.read().split("\n")]


i = 0
pos = 0
# path = [0, 3, 0, 1, -3]
solve = 'a'
while True:
    try:
        new_pos = (pos + path[pos])
        if solve == 'a':
            path[pos] += 1
        else:
            if path[pos] >= 3:
                path[pos] -= 1
            else:
                path[pos] += 1
        pos = new_pos
        i += 1
    except IndexError:
        print(i)
        break
