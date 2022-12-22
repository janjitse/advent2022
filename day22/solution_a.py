import re
import sys
import numpy as np

with open(sys.path[0] + "/input.txt", "r") as f:
    board_raw, instructions_raw = f.read().rstrip().split("\n\n")
locations = {}
line_start_ends = []
for i, line in enumerate(board_raw.split("\n")):
    line_start_ends.append([len(line.rstrip()), len(line.rstrip()) - 1])
    for j, c in enumerate(line.rstrip()):
        if c != " ":
            line_start_ends[-1][0] = min(line_start_ends[-1][0], j)
            locations[(i, j)] = c
max_length = max(max(line_start_ends, key=lambda x: x[1]))
print(max_length)
np_board = np.zeros((len(line_start_ends), max_length + 1), dtype=str)
np_board[:] = " "
for k in locations:
    np_board[k[0], k[1]] = locations[k]
column_start_ends = []
for col in range(max_length + 1):
    column_start_ends.append([max_length, 0])
    for i, row in enumerate(line_start_ends):
        if col >= row[0] and col <= row[1]:
            column_start_ends[-1][0] = min(column_start_ends[-1][0], i)
            column_start_ends[-1][1] = max(column_start_ends[-1][1], i)
# print(line_start_ends)
moves = re.findall(r"(\d+)([A-Z]?)", instructions_raw)
cur_loc = min(locations)
cur_dir = (0, 1)
path = set()
dir_dict = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
for mag, turn in moves:
    for _ in range(int(mag)):
        new_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])
        if new_loc in locations:
            if locations[new_loc] == ".":
                cur_loc = new_loc
                path.add(cur_loc)
            elif locations[new_loc] == "#":
                break
        else:
            if cur_dir[1] != 0:
                cur_line_start_end = line_start_ends[new_loc[0]]
                if new_loc[1] > cur_line_start_end[1]:
                    new_loc = (new_loc[0], cur_line_start_end[0])
                elif new_loc[1] < cur_line_start_end[0]:
                    new_loc = (new_loc[0], cur_line_start_end[1])
            elif cur_dir[0] != 0:
                cur_col_start_end = column_start_ends[new_loc[1]]
                if new_loc[0] > cur_col_start_end[1]:
                    new_loc = (cur_col_start_end[0], new_loc[1])
                if new_loc[0] < cur_col_start_end[0]:
                    new_loc = (cur_col_start_end[1], new_loc[1])
            if locations[new_loc] == ".":
                cur_loc = new_loc
                path.add(cur_loc)
            elif locations[new_loc] == "#":
                break
    if turn == "L":
        cur_dir = (-cur_dir[1], cur_dir[0])
    if turn == "R":
        cur_dir = (cur_dir[1], -cur_dir[0])

print(cur_loc, cur_dir)
print(1000 * (cur_loc[0] + 1) + 4 * (cur_loc[1] + 1) + dir_dict[cur_dir])

# part b
cur_loc = min(locations)
cur_dir = (0, 1)
path = []
# cur_loc = (51, 51)
# cur_dir = (0, -1)
# fake_moves = [("500", "")]
for mag, turn in moves:
    for _ in range(int(mag)):
        new_loc = (cur_loc[0] + cur_dir[0], cur_loc[1] + cur_dir[1])
        if new_loc in locations:
            if locations[new_loc] == ".":
                cur_loc = new_loc
                path.append([cur_loc, cur_dir])
            elif locations[new_loc] == "#":
                break
        else:
            if cur_dir[1] != 0:
                cur_line_start_end = line_start_ends[new_loc[0]]
                if new_loc[1] > cur_line_start_end[1]:  # move over right edge
                    if cur_loc[0] < 50:  # 2 -> 5
                        new_loc = (
                            149 - cur_loc[0],
                            99,
                        )
                        new_dir = (0, -cur_dir[1])
                    elif 50 <= cur_loc[0] < 100:  # 3 -> 2
                        new_loc = (49, 100 + (cur_loc[0] - 50))
                        new_dir = (-cur_dir[1], 0)
                    elif 100 <= cur_loc[0] < 150:  # 5 -> 2
                        new_loc = (
                            149 - cur_loc[0],
                            149,
                        )
                        new_dir = (0, -cur_dir[1])
                    elif 150 <= cur_loc[0] < 200:  # 6 -> 5
                        new_loc = (149, 50 + (cur_loc[0] - 150))
                        new_dir = (-cur_dir[1], 0)
                elif new_loc[1] < cur_line_start_end[0]:  # move over left edge
                    if cur_loc[0] < 50:  # 1-> 4
                        print("Move 1 to 4")
                        new_loc = (
                            149 - cur_loc[0],
                            0,
                        )
                        new_dir = (0, -cur_dir[1])
                    elif 50 <= cur_loc[0] < 100:  # 3 -> 4
                        new_loc = (100, cur_loc[0] - 50)
                        new_dir = (-cur_dir[1], 0)
                    elif 100 <= cur_loc[0] < 150:  # 4 -> 1
                        new_loc = (
                            149 - cur_loc[0],
                            50,
                        )
                        new_dir = (0, -cur_dir[1])
                    elif 150 < cur_loc[0]:  # 6 -> 1
                        new_loc = (0, 50 + (cur_loc[0] - 150))
                        new_dir = (-cur_dir[1], 0)
            elif cur_dir[0] != 0:
                cur_col_start_end = column_start_ends[new_loc[1]]
                if new_loc[0] > cur_col_start_end[1]:  # move over down edge
                    if cur_loc[1] < 50:  # 6 - > 2
                        print("Move 6 to 2")
                        new_loc = (0, 100 + cur_loc[1])
                        new_dir = (cur_dir[0], 0)
                        print(new_loc)
                        print(new_dir)
                    elif 50 <= cur_loc[1] < 100:  # 5 -> 6
                        new_loc = (150 + (cur_loc[1] - 50), 49)
                        new_dir = (0, -cur_dir[0])
                    elif 100 <= cur_loc[1] < 150:  # 2 -> 3
                        new_loc = (50 + (cur_loc[1] - 100), 99)
                        new_dir = (0, -cur_dir[0])
                elif new_loc[0] < cur_col_start_end[0]:  # move over top edge
                    if cur_loc[1] < 50:  # 4 - > 3
                        new_loc = (50 + cur_loc[1], 50)
                        new_dir = (0, -cur_dir[0])
                    elif 50 <= cur_loc[1] < 100:  # 1 -> 6
                        new_loc = (150 + (cur_loc[1] - 50), 0)
                        new_dir = (0, -cur_dir[0])
                    elif 100 <= cur_loc[1] < 150:  # 2 -> 6
                        new_loc = (199, cur_loc[1] - 100)
                        new_dir = (cur_dir[0], 0)
            if locations[new_loc] == ".":
                cur_loc = new_loc
                cur_dir = new_dir
                path.append([cur_loc, cur_dir])
            elif locations[new_loc] == "#":
                break
    if turn == "L":
        cur_dir = (-cur_dir[1], cur_dir[0])
    if turn == "R":
        cur_dir = (cur_dir[1], -cur_dir[0])

mov_dict = {(0, 1): ">", (1, 0): "v", (0, -1): "<", (-1, 0): "^"}
# print(np_board)
# for l in np_board:
#     print("".join(l))
for pos, mov in path:
    np_board[pos] = mov_dict[mov]
for l in np_board:
    print("".join(l))

print(cur_loc, cur_dir)
print(1000 * (cur_loc[0] + 1) + 4 * (cur_loc[1] + 1) + dir_dict[cur_dir])
