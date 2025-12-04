#! /usr/bin/env python

import sys
from collections import defaultdict

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


grid = defaultdict(lambda: ".")
max_y = len(lines)
for y, l in enumerate(lines):
    max_x = len(l)
    for x, c in enumerate(l):
        grid[x + y * 1j] = c


def neigh(p: complex) -> tuple[complex, ...]:
    return tuple(p + c for c in (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j))


def is_movable(p: complex) -> bool:
    return grid[p] == "@" and sum(grid[n] == "@" for n in neigh(p)) < 4


print("Part 1:", sum(is_movable(p) for p in tuple(grid.keys())))

result = 0
while True:
    new_moves = 0
    for y in range(max_y):
        for x in range(max_x):
            if is_movable(x + y * 1j):
                grid[x + y * 1j] = "."
                new_moves += 1
    if not new_moves:
        break
    result += new_moves

print("Part 2:", result)
