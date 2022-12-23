import sys

around_map = lambda x: {
    (x[0] + i, x[1] + j) for i in range(-1, 2) for j in range(-1, 2)
} - {(x[0], x[1])}

northish = lambda x: [(x[0] - 1, x[1] + i) for i in range(-1, 2)]
southish = lambda x: [(x[0] + 1, x[1] + i) for i in range(-1, 2)]
westish = lambda x: [(x[0] + i, x[1] - 1) for i in range(-1, 2)]
eastish = lambda x: [(x[0] + i, x[1] + 1) for i in range(-1, 2)]


def print_board(elf_pos, max_x, min_x, max_y, min_y):
    board = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for p in elf_pos:
        board[p[0] - min_y][p[1] - min_x] = "#"
    for l in board:
        print("".join(l))


move_list = [northish, southish, westish, eastish]
elves = {}
elf_count = 0
elf_locations = {}
elf_move_list = {}
with open(sys.path[0] + "/input.txt", "r") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == "#":
                elves[(i, j)] = elf_count
                elf_locations[elf_count] = (i, j)
                elf_move_list[elf_count] = move_list.copy()

                elf_count += 1
steps = 0

while True:
    steps += 1
    if steps % 100 == 0:
        print(steps)
    proposed = {}
    unmoved_elves = 0
    for elf in elves:
        around = around_map(elf)
        move = False
        for neighbor in around:
            if neighbor in elves:
                move = True
                break
        if move:
            mov_possible = True
            for mov_idx, check in enumerate(move_list):
                mov_possible = True
                scan = check(elf)
                # print(f"checking {scan} for elf at {elf}")
                for e in scan:
                    if e in elves:
                        mov_possible = False
                        break
                if mov_possible:
                    # elf_move_last[elves[elf]] = mov_idx
                    prop_move = (
                        scan[1][0],
                        scan[1][1],
                    )
                    # print(
                    #     f"elf {elves[elf]} proposes to move from {elf} to {prop_move}"
                    # )
                    if prop_move in proposed:
                        proposed[prop_move].append(elves[elf])
                    else:
                        proposed[prop_move] = [elves[elf]]
                    break
            if not mov_possible:
                unmoved_elves += 1
                # print(f"elf {elves[elf]} stays at {elf} ")
                proposed[elf] = [elves[elf]]
        else:
            # print(f"elf {elves[elf]} stays at {elf}")
            unmoved_elves += 1
            proposed[elf] = [elves[elf]]
    move_list.append(move_list.pop(0))
    # print(sum([len(c) for c in proposed.values()]))
    conflict_resolved = proposed.copy()
    for pos in proposed:
        if len(proposed[pos]) > 1:
            # print(f"Conflict at {pos}, elves that want to move here: {proposed[pos]}")
            for elf_c in proposed[pos]:
                unmoved_elves += 1
                conflict_resolved[elf_locations[elf_c]] = [elf_c]
            conflict_resolved[pos] = []
    # print(conflict_resolved)
    # print(len(proposed.items()))
    # print(unmoved_elves)
    if unmoved_elves == len(proposed.items()):
        break
    elves = {}
    elf_locations = {}

    for pos, elf_idx in conflict_resolved.items():
        if len(elf_idx) > 0:
            elves[pos] = elf_idx[0]
            elf_locations[elf_idx[0]] = pos
    if steps == 10:
        max_right = max(elves.keys(), key=lambda x: x[1])[1]
        min_right = min(elves.keys(), key=lambda x: x[1])[1]

        max_top = max(elves.keys(), key=lambda x: x[0])[0]
        min_top = min(elves.keys(), key=lambda x: x[0])[0]
        print(max_right, min_right, max_top, min_top)

        print((max_top - min_top + 1) * (max_right - min_right + 1) - len(elves))
        # print(len(elves.items()))
        # print(len(elf_locations.items()))

        print_board(elves, max_right, min_right, max_top, min_top)
        print("")


print(steps)
