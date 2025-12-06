#! /usr/bin/env python

import sys
from math import prod

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

ops = lines[-1].split()

lines_p1 = [l.split() for l in lines[:-1]]
numbers_p1 = [[int(l[i]) for l in lines_p1] for i in range(len(lines_p1[0]))]
result = sum(
    prod(numbers_p1[i]) if op == "*" else sum(numbers_p1[i]) for i, op in enumerate(ops)
)
print("Part 1:", result)

numbers_p2 = []
tmp = []
for i in range(len(lines[0]), 0, -1):
    n = "".join(l[i - 1] for l in lines[:-1])
    try:
        tmp.append(int(n))
    except ValueError:
        numbers_p2.append(tmp)
        tmp = []
if tmp:
    numbers_p2.append(tmp)

result = sum(
    prod(numbers_p2[i]) if op == "*" else sum(numbers_p2[i])
    for i, op in enumerate(ops[::-1])
)
print("Part 2:", result)
