#! /usr/bin/env python

import sys
from collections import defaultdict

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

max_y = len(lines)
max_x = len(lines[0])
manifold = {(x, y): c for y, l in enumerate(lines) for x, c in enumerate(l)}

result_p1 = 0
tmp = defaultdict(int)
tmp[lines[0].index("S"), 0] = 1
for y in range(1, max_y):
    for x in range(max_x):
        if manifold[x, y] == ".":
            tmp[x, y] += tmp[x, y - 1]
        elif manifold[x, y] == "^":
            result_p1 += tmp[x, y - 1] > 0
            tmp[x - 1, y] += tmp[x, y - 1]
            tmp[x + 1, y] += tmp[x, y - 1]

print("Part 1:", result_p1)
print("Part 2:", sum(tmp[x, max_y - 1] for x in range(max_x)))
