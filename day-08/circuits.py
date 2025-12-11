#! /usr/bin/env python

from __future__ import annotations

import sys
from dataclasses import dataclass
from math import prod

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


@dataclass(eq=True, frozen=True)
class Point:

    x: int
    y: int
    z: int

    def distance(self: Point, other: Point) -> float:
        return sum((getattr(self, c) - getattr(other, c)) ** 2 for c in "xyz")


points = [Point(*tuple(int(n) for n in l.split(","))) for l in lines]
connections = sorted(
    ((p1, p2) for i, p1 in enumerate(points) for p2 in points[i + 1 :]),
    key=lambda t: t[0].distance(t[1]),
)

circuits = []
connected = {p: {p} for p in points}
for i, (p1, p2) in enumerate(connections):
    if i == 1000:  # 10 for test
        circuits = set(frozenset(c) for c in connected.values())
        print(
            "Part 1:", prod(len(c) for c in sorted(circuits, key=len, reverse=True)[:3])
        )

    new_c = connected[p1] | connected[p2]
    for p in new_c:
        connected[p] = new_c

    if len(new_c) == len(points):
        print("Part 2:", p1.x * p2.x)
        break
