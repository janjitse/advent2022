import sys
import numpy as np

forest = []

with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        line = [int(c) for c in l.strip()]
        forest.append(line)
forest = np.array(forest)
print(forest.shape)

print(forest)
left_visible = np.zeros_like(forest)
for i in range(1, forest.shape[1]):
    for j in range(forest.shape[0]):
        visible = 1
        for k in range(i - 1, 0, -1):
            if forest[j, k] < forest[j, i]:
                visible += 1
            else:
                break
        left_visible[j, i] = visible

right_visible = np.zeros_like(forest)
for i in range(forest.shape[1] - 2, -1, -1):
    for j in range(forest.shape[0]):
        visible = 1
        for k in range(i + 1, forest.shape[1] - 1):
            if forest[j, k] < forest[j, i]:
                visible += 1
            else:
                break
        right_visible[j, i] = visible


top_visible = np.zeros_like(forest)
for i in range(1, forest.shape[0]):
    for j in range(forest.shape[1]):
        visible = 1
        for k in range(i - 1, 0, -1):
            if forest[k, j] < forest[i, j]:
                visible += 1
            else:
                break
        top_visible[i, j] = visible

bot_visible = np.zeros_like(forest)
for i in range(forest.shape[0] - 2, -1, -1):
    for j in range(forest.shape[1]):
        visible = 1
        for k in range(i + 1, forest.shape[0] - 1):
            if forest[k, j] < forest[i, j]:
                visible += 1
            else:
                break
        bot_visible[i, j] = visible
score = left_visible * right_visible * top_visible * bot_visible
print(np.max(score))
