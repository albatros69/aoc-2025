#! /usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


def move(pos: int, action: str) -> tuple[int, int]:
    direction = action[0]
    nb = int(action[1:])
    if direction == "R":
        new_pos = pos + nb
        return new_pos % 100, new_pos // 100
    else:
        new_pos = pos - nb
        return new_pos % 100, abs(new_pos // 100) - (pos == 0) + (new_pos % 100 == 0)


pos = 50
result_p1, result_p2 = 0, 0
for l in lines:
    pos, nb_zeros = move(pos, l)
    result_p1 += pos == 0
    result_p2 += nb_zeros
print("Part 1:", result_p1)
print("Part 2:", result_p2)
