#!/usr/bin/env python
"""
Advent of Code 2017 - Day 4 (http://adventofcode.com/2017/day/4)
"""
from collections import Counter

with open('data/day4.txt') as openfile:
    data = [line.strip().split() for line in openfile.read().split("\n")]


def solve_a():
    z = 0
    for entry in data:
        counted = dict(Counter(entry))
        if not any(counted[x] > 1 for x in counted):
            z += 1
    return z


def solve_b():
    z = 0
    for entry in data:
        broken = [Counter([x for x in x]) for x in entry]
        if not any(x for x in [broken[n] in (broken[:n] + broken[n + 1:]) for n in range(len(broken))]):
            z += 1
    return z

print(solve_a())
print(solve_b())


