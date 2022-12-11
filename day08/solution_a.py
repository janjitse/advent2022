import sys
import numpy as np

forest_list = []

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        forest_line = [int(c) for c in line.strip()]
        forest_list.append(forest_line)


forest = np.array(forest_list)
left_max = np.zeros_like(forest)
left_max[:, 0] = forest[:, 0]
visible_left = np.zeros_like(forest, dtype=bool)
visible_left[:, 0] = True
for i in range(1, forest.shape[1]):
    left_max[:, i] = np.max(np.array([forest[:, i], left_max[:, i - 1]]), axis=0)
    visible_left[:, i] = forest[:, i] > left_max[:, i - 1]

right_column = forest.shape[1] - 1
right_max = np.zeros_like(forest)
right_max[:, right_column] = forest[:, right_column]
visible_right = np.zeros_like(forest, dtype=bool)
visible_right[:, right_column] = True
for i in range(forest.shape[1] - 2, -1, -1):
    right_max[:, i] = np.max(np.array([forest[:, i], right_max[:, i + 1]]), axis=0)
    visible_right[:, i] = forest[:, i] > right_max[:, i + 1]

top_max = np.zeros_like(forest)
top_max[0, :] = forest[0, :]
visible_top = np.zeros_like(forest, dtype=bool)
visible_top[0, :] = True
for i in range(1, forest.shape[0]):
    top_max[i, :] = np.max(np.array([forest[i, :], top_max[i - 1, :]]), axis=0)
    visible_top[i, :] = forest[i, :] > top_max[i - 1, :]


bot_col = forest.shape[0] - 1
bot_max = np.zeros_like(forest)
bot_max[bot_col, :] = forest[bot_col, :]
visible_bot = np.zeros_like(forest, dtype=bool)
visible_bot[bot_col, :] = True
for i in range(forest.shape[0] - 2, -1, -1):
    bot_max[i, :] = np.max(np.array([forest[i, :], bot_max[i + 1, :]]), axis=0)
    visible_bot[i, :] = forest[i, :] > bot_max[i + 1, :]

visible = visible_left | visible_right | visible_top | visible_bot
print(np.sum(visible))
