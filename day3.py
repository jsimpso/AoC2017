#!/usr/bin/env python
"""Advent of Code 2017 - Day 3 (http://adventofcode.com/2017/day/3)"""


def gen_spiral(n):
    pattern = [[1, 2]]
    expanded = lambda x: [0] + [y for x in [x + x + x + x for x in x] for y in x]
    while len(expanded(pattern)) < n:
        start = pattern[-1][0] + 2
        end = start + 1
        middle = int(end / 2)
        # length = end digit
        next_pattern = [i for i in reversed(range(middle, start + 1))] + [i for i in range(middle + 1, end + 1)]
        pattern.append(next_pattern)
    return expanded(pattern)[n-1]


def gen_crazy_spiral(target):
    global data
    data = dict()
    data[0] = {'value': 1, 'location': (0, 0)}
    step = 0
    highval = lambda data_dict: max([int(data_dict[x]['value']) for x in data_dict])
    while highval(data) < target:
        step += 2
        move('right', 1)
        move('up', step-1)
        move('left', step)
        move('down', step)
        move('right', step)
    return min([int(data[x]['value']) for x in data if data[x]['value'] >= target])


def move(direction, repeats):
    global data
    for _ in range(repeats):
        index = sorted([x for x in data])[-1]
        location = data[index]['location']
        x = location[0]
        y = location[1]
        z = 0
        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1

        for entry in data:
            if (x - 1) <= data[entry]['location'][0] <= (x + 1) and (y - 1) <= data[entry]['location'][1] <= (y + 1):
                z += data[entry]['value']
        data[index + 1] = {'location': (x, y), 'value': z}


