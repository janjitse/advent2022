import sys
import re
from typing import List

start_board: List[List[str]] = []
moves = []
with open(sys.path[0] + "/input.txt", "r") as f:
    board = True
    ordA = ord("A")
    ordZ = ord("Z")
    for line in f:
        if not start_board:
            start_board = [[] for _ in range(0, len(line), 4)]
        if len(line.strip()) > 0 and board:
            if len(line) % 4 != 0:
                line = line[: len(line) // 4 * 4]
            for k in range(0, len(line), 4):
                if ordA <= ord(line[k + 1]) <= ordZ:
                    start_board[k // 4] += line[k + 1 : k + 2]
        if len(line.strip()) == 0:
            board = False
        if len(line.strip()) > 0 and not board:
            to_parse = re.findall(r"\d+", line)
            moves.append([int(t) for t in to_parse])


print("Start moving")
for i, m in enumerate(moves):
    if i % 1000 == 0:
        print(f"Moved {i} times")
    from_pos = m[1] - 1
    to_pos = m[2] - 1
    amount = m[0]

    start_board[to_pos] = start_board[from_pos][:amount] + start_board[to_pos]
    start_board[from_pos] = start_board[from_pos][amount:]

message = "".join([k[0] if k else "_" for k in start_board])
print(message)
