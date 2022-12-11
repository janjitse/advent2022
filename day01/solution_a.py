import sys
from typing import List


elves_calories: List[List[int]] = []
elves_total = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not elves_calories or len(line) == 0:
            elves_calories.append([])
        if len(line) > 0:
            elves_calories[-1].append(int(line))
        else:
            elves_total.append(sum(elves_calories[-2]))
elves_total.append(sum(elves_calories[-1]))
print(max(elves_total))
print(sum(sorted(elves_total)[-3:]))
