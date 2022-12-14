import sys
from typing import List, Tuple

paths: List[List[Tuple[int, int]]] = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        points = line.strip().split(" -> ")
        paths.append([])
        for p in points:
            coord = p.split(",")
            paths[-1].append((int(coord[0]), int(coord[1])))

all_points = [p for line in paths for p in line]
board_x = max(all_points, key=lambda p: p[0])[0]
board_y = max(all_points, key=lambda p: p[1])[1]

# print(board_x, board_y)
blocked = set()
for path in paths:
    for i, point in enumerate(path[1:], 1):
        prev_point = path[i - 1]
        if point[0] == prev_point[0]:
            top = min([point[1], prev_point[1]])
            bottom = max([point[1], prev_point[1]])
            for y in range(top, bottom + 1):
                blocked.add((point[0], y))

        if point[1] == prev_point[1]:
            left = min([point[0], prev_point[0]])
            right = max([point[0], prev_point[0]])
            for x in range(left, right + 1):
                blocked.add((x, point[1]))
sand_counter = 0
steps = [(0, 1), (-1, 1), (1, 1)]
source_blocked = False
while not source_blocked:
    sand_pos = (500, 0)
    sand_counter += 1
    if sand_counter % 1000 == 0:
        print(sand_counter)
    while True:
        next_possible = False
        for step in steps:
            trial_pos = (sand_pos[0] + step[0], sand_pos[1] + step[1])

            if (trial_pos[0], trial_pos[1]) not in blocked and sand_pos[
                1
            ] < board_y + 1:
                sand_pos = (trial_pos[0], trial_pos[1])
                next_possible = True
        if not next_possible:
            blocked.add((sand_pos[0], sand_pos[1]))
            if sand_pos[0] == 500 and sand_pos[1] == 0:
                source_blocked = True
            break
print(sand_counter)
