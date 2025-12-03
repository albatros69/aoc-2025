#! /usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


def max_joltage(batteries: str, n: int):
    if not batteries:
        raise ValueError
    elif len(batteries) == n + 1:
        return batteries
    elif n == 0:
        return max(batteries)
    else:
        m = max(batteries[:-n])
        i = batteries.index(m) + 1
        return m + max_joltage(batteries[i:], n - 1)


print("Part 1:", sum(int(max_joltage(l, 1)) for l in lines))
print("Part 2:", sum(int(max_joltage(l, 11)) for l in lines))
