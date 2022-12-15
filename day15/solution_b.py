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

frequency = 0
for line_to_check in range(4000000 + 1):
    if line_to_check % 100000 == 0:
        print(line_to_check)
    impossible = []
    for (x, y), distance in sensors.items():
        dist_y = abs(y - line_to_check)
        if dist_y <= distance:
            x_min = x - distance + dist_y
            x_max = x + distance - dist_y
            impossible.append((x_min, x_max))
    impossible = sorted(impossible, key=lambda x: x[0])
    merged_impossible = [list(impossible[0])]
    for x, y in impossible[1:]:
        if x <= merged_impossible[-1][1] + 1:
            merged_impossible[-1][1] = max(y, merged_impossible[-1][1])
        else:
            merged_impossible.append([x, y])
    if len(merged_impossible) > 1:
        frequency = (merged_impossible[0][1] + 1) * 4000000 + line_to_check

print(frequency)
