import sys
import numpy as np

board = []

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        board.append([ord(c) - ord("a") for c in line.strip()])
board_np = np.array(board)
start_pos = np.where(board_np == (ord("S") - ord("a")))
end_pos = np.where(board_np == (ord("E") - ord("a")))

board_np[start_pos[0], start_pos[1]] = 0
board_np[end_pos[0], end_pos[1]] = ord("z") - ord("a")

infinity = board_np.shape[0] * board_np.shape[1] + 1

lengths = np.zeros_like(board_np) + infinity
lengths[start_pos[0], start_pos[1]] = 0
lengths = np.where(board_np == 0, 0, lengths)

up_possible = (board_np[:-1, :] - board_np[1:, :]) <= 1

down_possible = (board_np[1:, :] - board_np[:-1, :]) <= 1
right_possible = (board_np[:, 1:] - board_np[:, :-1]) <= 1

left_possible = (board_np[:, :-1] - board_np[:, 1:]) <= 1

for i in range(infinity):
    lengths_so_far = lengths.copy()
    tmp_left = np.hstack(
        [
            np.where(
                left_possible,
                np.minimum(lengths_so_far[:, :-1], lengths_so_far[:, 1:] + 1),
                lengths_so_far[:, :-1],
            ),
            lengths_so_far[:, -1:],
        ]
    )
    tmp_right = np.hstack(
        [
            lengths_so_far[:, :1],
            np.where(
                right_possible,
                np.minimum(lengths_so_far[:, :-1] + 1, lengths_so_far[:, 1:]),
                lengths_so_far[:, 1:],
            ),
        ]
    )
    tmp_down = np.vstack(
        [
            lengths_so_far[:1, :],
            np.where(
                down_possible,
                np.minimum(lengths_so_far[1:, :], lengths_so_far[:-1, :] + 1),
                lengths_so_far[1:, :],
            ),
        ]
    )
    tmp_up = np.vstack(
        [
            np.where(
                up_possible,
                np.minimum(lengths_so_far[:-1, :], lengths_so_far[1:, :] + 1),
                lengths_so_far[:-1, :],
            ),
            lengths_so_far[-1:, :],
        ]
    )
    lengths = np.min(np.stack([tmp_up, tmp_down, tmp_left, tmp_right]), axis=0)
print(lengths[end_pos[0], end_pos[1]])
