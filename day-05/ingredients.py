#! /usr/bin/env python

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

flag = True
fresh_inventory = []
ingredients = []
for l in lines:
    if not l:
        flag = False
        continue
    if flag:
        a, b = (int(c) for c in l.split("-"))
        fresh_inventory.append(range(a, b + 1))
    else:
        ingredients.append(int(l))


def is_fresh(ingredient: int) -> bool:
    return any(ingredient in fresh for fresh in fresh_inventory)


print("Part 1:", sum(is_fresh(i) for i in ingredients))


def compact(inventory: list) -> int:
    if not inventory:
        return 0
    if len(inventory) == 1:
        return len(inventory[0])

    r1, r2, *l = inventory
    if r2.start > r1.stop:
        return len(r1) + compact(inventory[1:])
    else:
        return compact([range(r1.start, max(r1.stop, r2.stop))] + l)


fresh_inventory.sort(key=lambda r: r.start)
print("Part 2:", compact(fresh_inventory))
