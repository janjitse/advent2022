import sys
from itertools import cycle
import numpy as np
from typing import Dict, Tuple

blocks_list = [
    np.array([[1, 1, 1, 1]], dtype=bool),
    np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=bool),
    np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]][::-1], dtype=bool),
    np.array([[1], [1], [1], [1]], dtype=bool),
    np.array([[1, 1], [1, 1]], dtype=bool),
]


with open(sys.path[0] + "/input.txt", "r") as f:
    moves_list = [-1 if c == "<" else +1 for c in f.read().strip()]


max_range = 8000
board = np.zeros((4 * max_range, 7), dtype=bool)
moves = cycle(moves_list)
blocks = cycle(blocks_list)
highest_rock = 0
move_idx = 0
pattern_dict: Dict[Tuple[int, int, Tuple[bool, ...]], int] = {}
height_list = []
for block_idx in range(max_range):
    block = next(blocks)
    stopped = False
    left_edge = 2
    bottom_edge = highest_rock + 3
    while not stopped:
        move = next(moves)
        move_idx += 1
        trial_move = left_edge + move
        if trial_move >= 0 and trial_move + block.shape[1] <= 7:
            board_tile = board[
                bottom_edge : bottom_edge + block.shape[0],
                trial_move : trial_move + block.shape[1],
            ]

            if np.all(~(board_tile & block)):
                left_edge = trial_move

        trial_down = bottom_edge - 1
        if trial_down < 0:
            stopped = True
        else:
            board_tile = board[
                trial_down : trial_down + block.shape[0],
                left_edge : left_edge + block.shape[1],
            ]
            if np.all(~(board_tile & block)):
                bottom_edge = trial_down
            else:
                stopped = True
        if stopped:
            board[
                bottom_edge : bottom_edge + block.shape[0],
                left_edge : left_edge + block.shape[1],
            ] += block
            highest_rock = max(bottom_edge + block.shape[0], highest_rock)

    height_list.append(highest_rock)
    topn_rows = tuple(np.ravel(board[highest_rock - 14 : highest_rock + 1, :]))
    pattern = (block_idx % 5, move_idx % len(moves_list), topn_rows)
    if pattern in pattern_dict:
        print(f"Repeat found at rock {block_idx}")
        repeater_period = block_idx - pattern_dict[pattern]
        repeat_start = pattern_dict[pattern]
        break
    else:
        pattern_dict[pattern] = block_idx

rocks = 1000000000000
# rocks = 2022
print(f"Period: {repeater_period}")
print(f"First occurence: {repeat_start}")
initial = rocks % repeater_period
while initial < repeat_start:
    initial += repeater_period
nr_periods = (rocks - initial) // repeater_period

diff = height_list[repeat_start + repeater_period] - height_list[repeat_start]
print(f"Height increase per period: {diff}")

print(diff * nr_periods + height_list[initial] - 1)
