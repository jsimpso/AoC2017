#!/usr/bin/env python
"""
Advent of Code 2017 - Day 2 (http://adventofcode.com/2017/day/2)

Assumptions made:
    * Since the puzzle data provided is formatted with tabs, it is assumed that the puzzle input will see cells
      seperated by \t, and rows seperated by /n.

    * Puzzle input will be ready from a file
"""


def read_input(target_file):
    try:
        with open(target_file, 'r') as openfile:
            contents = openfile.read()
        return contents.strip().split("\n")
    except FileNotFoundError:
        print("File not found!")
        exit(1)


def solve_a():
    input_val = read_input("data/day2_input.val")
    result = 0
    for row in input_val:
        nums = [int(x) for x in row.split("\t")]
        low = min(nums)
        high = max(nums)
        result += (int(high) - int(low))
    return result


def solve_b():
    input_val = read_input("data/day2_input.val")
    result = 0
    for row in input_val:
        nums = [int(x) for x in row.split("\t")]
        for num in nums:
            compatible = [x for x in nums if num % x == 0 and x != num]
            if len(compatible) == 1:
                result += max([num, compatible[0]])/min([num, compatible[0]])
    return result

print("Solution A: {answer}".format(answer=solve_a()))
print("Solution B: {answer}".format(answer=solve_b()))
