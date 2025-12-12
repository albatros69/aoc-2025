#! /usr/bin/env python

import sys
from functools import cache

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

devices = {l[:3]: [a for a in l[5:].split()] for l in lines}


@cache
def count_paths_p1(node: str) -> int:
    if node == "out":
        return 1

    return sum(count_paths_p1(d) for d in devices[node])


if "you" in devices:
    print("Part 1:", count_paths_p1("you"))


@cache
def count_paths_p2(node: str, dac: bool, fft: bool) -> int:
    if node == "out":
        return int(dac and fft)

    return sum(
        count_paths_p2(d, dac or (d == "dac"), fft or (d == "fft"))
        for d in devices[node]
    )


if "svr" in devices:
    print("Part 2:", count_paths_p2("svr", False, False))
