import sys


elves_calories = []
elves_total = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        l = l.strip()
        if not elves_calories or len(l) == 0:
            elves_calories.append([])
        if len(l) > 0:
            elves_calories[-1].append(int(l))
        else:
            elves_total.append(sum(elves_calories[-2]))
elves_total.append(sum(elves_calories[-1]))
print(max(elves_total))
print(sum(sorted(elves_total)[-3:]))
