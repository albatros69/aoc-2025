#! /usr/bin/env python

import sys
from operator import mul

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

tiles = [tuple(int(a) for a in l.split(",")) for l in lines]


def area(a, b):
    return mul(*(abs(a[i] - b[i]) + 1 for i in (0, 1)))


all_tuples = [(a, b) for i, a in enumerate(tiles) for b in tiles[i:]]

print("Part 1:", max(area(*t) for t in all_tuples))


def edge(a, b) -> set:
    s, e = min(a, b), max(a, b)
    if s[0] == e[0]:
        return {(s[0], i) for i in range(s[1], e[1] + 1)}
    else:
        return {(i, s[1]) for i in range(s[0], e[0] + 1)}


def frontiers(l_pt: list[tuple]) -> set:
    if len(l_pt) <= 1:
        return set()

    a, b, *_ = l_pt
    return set.union(edge(a, b), frontiers(l_pt[1:]))


tmp_frontiers = frontiers(tiles + tiles[:1])


def is_internal(a, b):
    xa, xb = sorted((a[0], b[0]))
    ya, yb = sorted((a[1], b[1]))
    return not any(xa < p[0] < xb and ya < p[1] < yb for p in tmp_frontiers)


all_tuples.sort(key=lambda t: area(*t), reverse=True)
for t in all_tuples:
    if is_internal(*t):
        print("Part 2:", area(*t))
        break
