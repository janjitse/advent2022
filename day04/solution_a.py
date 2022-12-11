import sys

assignments = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        assignments.append(
            [[int(m) for m in k.split("-")] for k in line.strip().split(",")]
        )
fully_contained = 0
overlap = 0

for a, b in assignments:
    range_1 = set(range(a[0], a[1] + 1))
    range_2 = set(range(b[0], b[1] + 1))

    if range_1 <= range_2 or range_2 <= range_1:
        fully_contained += 1
    if range_1.intersection(range_2):
        overlap += 1

print(fully_contained)
print(overlap)
