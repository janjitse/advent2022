import sys
import numpy as np


moves = []

direction_dict = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        direction, nr_steps = line.strip().split(" ")

        moves.append((direction, int(nr_steps)))
pos_h = [0, 0]
tail_positions = [[0, 0] for _ in range(9)]
been = set()


def sign(i: int) -> int:
    if i > 0:
        return 1
    if i < 0:
        return -1
    else:
        return 0


for dir, size in moves:
    mov = direction_dict[dir]
    for step in range(size):
        pos_h[0] = pos_h[0] + mov[0]
        pos_h[1] = pos_h[1] + mov[1]
        for i, pos_t in enumerate(tail_positions):
            if i == 8:
                been.add(tuple(pos_t))
            if i == 0:
                pos_prev = pos_h
            else:
                pos_prev = tail_positions[i - 1]
            if max([abs(pos_t[0] - pos_prev[0]), abs(pos_t[1] - pos_prev[1])]) > 1:
                tail_positions[i][0] = pos_t[0] + sign(pos_prev[0] - pos_t[0])
                tail_positions[i][1] = pos_t[1] + sign(pos_prev[1] - pos_t[1])
been.add(tuple(tail_positions[-1]))

print(len(been))


size_x = max(been, key=lambda x: x[0])[0] - min(been, key=lambda x: x[0])[0]
size_y = max(been, key=lambda x: x[1])[1] - min(been, key=lambda x: x[1])[1]
array = np.array([["." for _ in range(size_x)] for _ in range(size_y)])
midpoints = [size_x // 2, size_y // 2]
for (x, y) in been:
    array[x - midpoints[0], y - midpoints[1]] = "#"

for line in array:
    print("".join(line))
