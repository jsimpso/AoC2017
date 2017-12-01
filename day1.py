#!/usr/bin/env python
"""
Advent of Code 2017 - Day 1 (http://adventofcode.com/2017/day/1)
"""


def is_valid(input_val):
    try:
        int(input_val)
        if len(input_val) % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        return False


def solve_a(value):
    z = 0
    x = len(value)
    for i in range(x-1):
        if value[i] == value[i+1]:
            z += int(value[i])
    if value[0] == value[-1]:
        z += int(value[0])
    return z


def solve_b(value):
    z = 0
    x = len(value)
    step = int(len(value) / 2)
    for i in range(x):
        target = i + step
        if target > len(value)-1:
            target = target - x
        if value[i] == value[target]:
            z += int(value[i])
    return z


if __name__ == "__main__":
    input_val = ''
    while not is_valid(input_val):
        input_val = input("Please enter valid input value: ")

    puzzle = ''
    while puzzle not in ['A', 'B']:
        puzzle = input("Solve puzzle A, or Puzzle B: ").upper()

    if puzzle == 'A':
        result = solve_a(input_val)
    elif puzzle == 'B':
        result = solve_b(input_val)

    print("Output = {output}".format(output=result))
