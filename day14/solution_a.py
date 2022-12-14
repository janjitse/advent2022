import sys
import numpy as np
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

print(board_x, board_y)
board = np.zeros((board_y + 1, board_x + 1))
for path in paths:
    for i, point in enumerate(path[1:], 1):
        prev_point = path[i - 1]
        if point[0] == prev_point[0]:
            top = min([point[1], prev_point[1]])
            bottom = max([point[1], prev_point[1]])
            board[top : bottom + 1, point[0]] = 1

        if point[1] == prev_point[1]:
            left = min([point[0], prev_point[0]])
            right = max([point[0], prev_point[0]])
            board[point[1], left : right + 1] = 1

sand_counter = 0
steps = [(0, 1), (-1, 1), (1, 1)]
off_board = False
while not off_board:
    sand_pos = (500, 0)
    sand_counter += 1
    while True:
        next_possible = False
        for step in steps:
            trial_pos = (sand_pos[0] + step[0], sand_pos[1] + step[1])
            if trial_pos[1] > board_y:
                off_board = True
                break
            if board[trial_pos[1], trial_pos[0]] == 0:
                sand_pos = (trial_pos[0], trial_pos[1])
                next_possible = True
                break
        if not next_possible:
            board[sand_pos[1], sand_pos[0]] = 1
            break
        if off_board:
            break
print(sand_counter - 1)
