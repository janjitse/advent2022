import sys
from collections import deque
import heapq

blizzards = {
    ">": set(),
    "<": set(),
    "^": set(),
    "v": set(),
}
mov = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}


def print_board(blizzards, max_len, max_height, cur_pos=None):
    board = [["."] * max_len for _ in range(max_height)]
    for b in blizzards:
        for c in blizzards[b]:
            board[c[0]][c[1]] = b
    if cur_pos:
        board[cur_pos[0]][cur_pos[1]] = "E"
    for l in board:
        print("".join(l))


next_step_map = lambda x: [
    (x[0], x[1]),
    (x[0] + 1, x[1]),
    (x[0] - 1, x[1]),
    (x[0], x[1] + 1),
    (x[0], x[1] - 1),
]

max_len = 0
max_height = 0
with open(sys.path[0] + "/input.txt", "r") as f:
    for i, l in enumerate(f):
        max_height = max(max_height, i)
        max_len = max(len(l), max_len)
        for j, c in enumerate(l):
            if c in blizzards:
                blizzards[c].add((i - 1, j - 1))

max_len = max_len - 3
max_height = max_height - 1
print(max_len)
print(max_height)
lcm = 600
print_board(blizzards, max_len, max_height)
blizzards_time_step = []
for step in range(1, lcm + 1):
    new_blizzards = {
        ">": set(),
        "<": set(),
        "^": set(),
        "v": set(),
    }
    blizzards_time_step.append(set())
    for b in blizzards:
        for c in blizzards[b]:
            new_pos = ((c[0] + mov[b][0]) % max_height, (c[1] + mov[b][1]) % max_len)
            new_blizzards[b].add(new_pos)
            blizzards_time_step[-1].add(c)
    blizzards = new_blizzards.copy()


def search(start_pos, end_pos, start_time):
    pos_seen = set()
    queue = [(start_time, start_pos)]
    shortest_path = None
    heapq.heapify(queue)
    while queue:
        time, pos = heapq.heappop(queue)
        if (
            shortest_path
            and end_pos[0] - pos[0] + end_pos[1] - pos[1] + time >= shortest_path
        ):
            continue

        next_steps = next_step_map(pos)
        for d in next_steps:
            if d == end_pos:
                if shortest_path:
                    shortest_path = min(shortest_path, time + 1)
                else:
                    shortest_path = time + 1
                break
            elif 0 <= d[0] < max_height and 0 <= d[1] < max_len or d == start_pos:
                if (
                    d not in blizzards_time_step[(time + 1) % lcm]
                    and (time + 1, d) not in pos_seen
                ):
                    if not shortest_path or (
                        end_pos[1] - d[1] + end_pos[0] - d[0] + time + 1 < shortest_path
                    ):
                        heapq.heappush(queue, (time + 1, d))
                        pos_seen.add((time + 1, d))
    return shortest_path


end_pos = (max_height, max_len - 1)
start_pos = (-1, 0)


forth = search(start_pos, end_pos, 0)
print(forth)
back = search(end_pos, start_pos, forth)
print(back)
and_back = search(start_pos, end_pos, back)
print(and_back)

start_time = 0
repeater = {}
target = 10_000
i = 0
while True:
    forth = search(start_pos, end_pos, start_time)
    back = search(end_pos, start_pos, forth)
    start_time = back
    if (forth % lcm, back % lcm) in repeater:
        period = i - repeater[(forth % lcm, back % lcm)][0]
        repeater[(forth, back)] = (i, (forth, back))
        break
    else:
        repeater[(forth % lcm, back % lcm)] = (i, (forth, back))
    i += 1

start_repeat = i - period
increase_per_period = forth - repeater[(forth % lcm, back % lcm)][1][0]
nr_repeats = (target - start_repeat) // period
offset = (target - start_repeat) % period + 1

for b, (v1, v2) in repeater.values():
    if b == offset + start_repeat:
        print(v1 + nr_repeats * increase_per_period)
        break
