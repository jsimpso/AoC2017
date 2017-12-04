#!/usr/bin/env python
"""WIP"""
import itertools


def gen_pattern(n):
        pattern = [[1, 2]]
        while len(pattern) < n:
            start = pattern[-1][0]+2
            end = start + 1
            middle = int(end / 2)
            # length = end digit
            next_pattern = [i for i in reversed(range(middle, start+1))] + [i for i in range(middle+1, end+1)]
            pattern.append(next_pattern)
        return pattern


def gen_spiral(n):
    pattern = [[1, 2]]
    expanded = (lambda x: [y for x in [x + x + x + x for x in x] for y in x])(pattern)
    while len(expanded) < n:
        start = pattern[-1][0] + 2
        end = start + 1
        middle = int(end / 2)
        # length = end digit
        next_pattern = [i for i in reversed(range(middle, start + 1))] + [i for i in range(middle + 1, end + 1)]
        pattern.append(next_pattern)
        expanded = (lambda x: [y for x in [x + x + x + x for x in x] for y in x])(pattern)
    return expanded[n]


