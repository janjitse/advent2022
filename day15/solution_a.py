import sys
import re

beacons = set()
sensors = dict()
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        nrs = re.findall(r"(-?\d+)", line)
        sensors[(int(nrs[0]), int(nrs[1]))] = abs(int(nrs[0]) - int(nrs[2])) + abs(
            int(nrs[1]) - int(nrs[3])
        )
        beacons.add((int(nrs[2]), int(nrs[3])))

# line_to_check = 10
line_to_check = 2000000
beacons_on_line = 0
for (x, y) in beacons:
    if y == line_to_check:
        beacons_on_line += 1
impossible = []
for (x, y), distance in sensors.items():
    dist_y = abs(y - line_to_check)
    x_min = x - distance + dist_y
    x_max = x + distance - dist_y
    if x_min <= x_max:
        impossible.append((x_min, x_max))
impossible = sorted(impossible, key=lambda x: x[0])
print(impossible)
merged_impossible = [list(impossible[0])]
for x, y in impossible[1:]:
    if x <= merged_impossible[-1][1] + 1:
        merged_impossible[-1][1] = max(y, merged_impossible[-1][1])
    else:
        merged_impossible.append([x, y])
print(merged_impossible)
total_impossible = 0
for [x, y] in merged_impossible:
    total_impossible += (y - x) + 1
print(beacons_on_line)
print(total_impossible - beacons_on_line)
