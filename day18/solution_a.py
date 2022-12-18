import sys
import numpy as np
from collections import deque

obsidians = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        obsidians.append(tuple([int(d) for d in line.strip().split(",")]))

obsidians_np = np.array(obsidians)
size = np.max(obsidians_np)
obsidian_block = np.zeros((size + 3, size + 3, size + 3))
for (x, y, z) in obsidians:
    obsidian_block[x + 1, y + 1, z + 1] = 1

total_edges = 0
for axis in range(3):
    total_edges += np.sum(np.diff(obsidian_block, axis=axis) != 0)


print(total_edges)

water_fill = obsidian_block.copy()
queue = deque()
queue.append((0, 0, 0))

while queue:
    to_fill = queue.popleft()
    if water_fill[to_fill[0], to_fill[1], to_fill[2]] > 0:
        continue
    water_fill[to_fill[0], to_fill[1], to_fill[2]] = 2
    for axis in range(3):
        att = to_fill[:axis] + (to_fill[axis] + 1,) + to_fill[axis + 1 :]
        att = tuple(att)
        if att[axis] < size + 3:
            if water_fill[att[0], att[1], att[2]] == 0:
                queue.append(att)
        att = to_fill[:axis] + (to_fill[axis] - 1,) + to_fill[axis + 1 :]
        if att[axis] > 0:
            if water_fill[att[0], att[1], att[2]] == 0:
                queue.append(att)

obsidian_block_water = np.where(water_fill == 2, 0, 1)


total_edges_water = 0
for axis in range(3):
    total_edges_water += np.sum(np.diff(obsidian_block_water, axis=axis) != 0)
print(total_edges_water)
