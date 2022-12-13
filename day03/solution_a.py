import sys

rucksacks = []

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        rucksack_total = line.strip()
        item_len = len(rucksack_total) // 2
        rucksacks.append([rucksack_total[:item_len], rucksack_total[item_len:]])

common_items = []
for line, r in rucksacks:
    common = list(set(list(line)).intersection(set(list(r))))
    common_items += common

total_priority = 0


def priority_calc(c: str) -> int:
    if c.isupper():
        priority = (ord(c) - ord("A") + 1) + 26
    else:
        priority = ord(c) - ord("a") + 1
    return priority


for c in common_items:
    total_priority += priority_calc(c)

print(total_priority)

all_badges = []
for k in range(0, len(rucksacks), 3):
    rucksack_1 = set(list(rucksacks[k][0] + rucksacks[k][1]))
    rucksack_2 = set(list(rucksacks[k + 1][0] + rucksacks[k + 1][1]))
    rucksack_3 = set(list(rucksacks[k + 2][0] + rucksacks[k + 2][1]))
    badge = list(rucksack_1.intersection(rucksack_2).intersection(rucksack_3))
    all_badges += badge
badge_priority = 0
for b in all_badges:
    badge_priority += priority_calc(b)

print(badge_priority)
