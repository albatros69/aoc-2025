#! /usr/bin/env python

import re
import sys
from ast import literal_eval
from heapq import heappop, heappush

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


re_line = re.compile(r"^\[([.#]+)\] (.+) \{([0-9,]+)\}$")


class Machine:
    end_status: tuple[bool, ...]
    buttons: tuple[tuple[int, ...], ...]
    joltage_req: tuple[int, ...]

    def __init__(self, l: str):
        matches = re_line.match(l)
        self.end_status = tuple(c == "#" for c in matches.group(1))
        self.buttons = tuple(
            tuple((literal_eval(t),)) if len(t) <= 3 else literal_eval(t)
            for t in matches.group(2).split()
        )
        self.joltage_req = literal_eval(matches.group(3))

    def __str__(self) -> str:
        return (
            f"[{''.join('#' if a else '.' for a in self.end_status)}]"
            f" {self.buttons} {self.joltage_req}"
        )

    def __repr__(self) -> str:
        return str(self)

    def push_p1(self, button: int, status: list[bool]) -> tuple[bool, ...]:
        return tuple(
            not b if i in self.buttons[button] else b for i, b in enumerate(status)
        )

    def push_p2(self, button: int, joltage: list[int]) -> tuple[int, ...]:
        return tuple(
            b + 1 if i in self.buttons[button] else b for i, b in enumerate(joltage)
        )

    def dist_joltage(self, status) -> int:
        return max(
            abs(self.joltage_req[i] - status[i]) for i in range(len(self.joltage_req))
        )

    def power_up(self) -> int:

        queue = [(0, (False,) * len(self.end_status))]
        already_seen = {}
        while queue:
            nb, status = heappop(queue)

            if status == self.end_status:
                return nb

            if already_seen.get(status, float("inf")) <= nb:
                continue

            already_seen[status] = nb

            for i in range(len(self.buttons)):
                heappush(queue, (nb + 1, self.push_p1(i, status)))

        return 0

    def configure(self) -> int:

        status = (0,) * len(self.joltage_req)
        queue = [(self.dist_joltage(status), 0, (0,) * len(self.buttons), status)]
        # queue = [(self.dist_joltage(status), (0,) * len(self.buttons), status)]
        # queue = [(0, (0,) * len(self.buttons), status)]
        already_seen = set()
        while queue:
            _, nb, cpt_buttons, status = heappop(queue)
            # if len(queue) % 100 == 0:
            #     print(f"{len(queue):5}", nb, end="\r")

            if status == self.joltage_req:
                print(self, status, nb)
                return nb

            # if already_seen.get(cpt_buttons, float("inf")) <= sum(cpt_buttons):
            if cpt_buttons in already_seen:
                continue
            if any(a > self.joltage_req[i] for i, a in enumerate(status)):
                continue

            already_seen.add(cpt_buttons)

            for i in range(len(self.buttons)):
                new_status = self.push_p2(i, status)
                new_cpt_buttons = tuple(
                    c + 1 if j == i else c for j, c in enumerate(cpt_buttons)
                )
                if (
                    all(a <= self.joltage_req[i] for i, a in enumerate(new_status))
                    and new_cpt_buttons not in already_seen
                    # and already_seen.get(new_cpt_buttons, float("inf")) > sum(cpt_buttons)
                ):
                    heappush(
                        queue,
                        (
                            self.dist_joltage(new_status),
                            nb + 1,
                            new_cpt_buttons,
                            new_status,
                        ),
                    )

        return 0


machines = [Machine(l) for l in lines]
print("Part 1:", sum(m.power_up() for m in machines))
# Works only on tests and some lines of the inputs. Fails on some
# others unfortunately... Reddit points to Z3 linear solver.
# print("Part 2:", sum(m.configure() for m in machines))
