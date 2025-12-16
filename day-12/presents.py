#! /usr/bin/env python

import sys
from itertools import product

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


presents = []
trees = []
for i, l in enumerate(lines):
    if l.endswith(":"):
        presents.append(
            {
                (x, y): lines[i + 1 + y][x] == "#"
                for (x, y) in product(range(3), repeat=2)
            }
        )
    elif "x" in l:
        w, h = l[: l.index(":")].split("x")
        trees.append(
            {
                "w": int(w),
                "h": int(h),
                "reqs": tuple(int(n) for n in l[l.index(":") + 2 :].split()),
            }
        )


def area(present) -> int:
    return sum(present)


print(
    "Part 1:",
    sum(
        t["w"] * t["h"]
        >= sum(n * area(presents[i].values()) for i, n in enumerate(t["reqs"]))
        for t in trees
    ),
)
