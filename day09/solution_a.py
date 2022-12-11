import sys

moves = []

direction_dict = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        direction, nr_steps = line.strip().split(" ")

        moves.append((direction, int(nr_steps)))
pos_h = [0, 0]
pos_t = [0, 0]
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
        been.add(tuple(pos_t))
        pos_h[0] = pos_h[0] + mov[0]
        pos_h[1] = pos_h[1] + mov[1]
        if max([abs(pos_t[0] - pos_h[0]), abs(pos_t[1] - pos_h[1])]) > 1:
            pos_t[0] = pos_t[0] + sign(pos_h[0] - pos_t[0])
            pos_t[1] = pos_t[1] + sign(pos_h[1] - pos_t[1])
been.add(tuple(pos_t))

print(len(been))
