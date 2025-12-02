#! /usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


def is_invalid_p1(prod_id: str):
    l = len(prod_id) // 2
    return prod_id[:l] == prod_id[l:]


result = 0
for interval in lines[0].split(","):
    start, end = (int(a) for a in interval.split("-"))
    result += sum(a for a in range(start, end + 1) if is_invalid_p1(str(a)))
print("Part 1:", result)


def is_invalid_p2(prod_id: str):
    l = len(prod_id)
    return any(prod_id == prod_id[:i] * (l // i) for i in range(1, l // 2 + 1))


result = 0
for interval in lines[0].split(","):
    start, end = (int(a) for a in interval.split("-"))

    result += sum(a for a in range(start, end + 1) if is_invalid_p2(str(a)))
print("Part 2:", result)
