import sys

from utils import stupid_parser, recurse_greater


all_signals = []
with open(sys.path[0] + "/input.txt", "r") as f:
    signals = f.read().strip().split("\n\n")
    for signal in signals:
        s1, s2 = signal.split("\n")
        list1 = stupid_parser(s1)
        list2 = stupid_parser(s2)
        all_signals.append(list1)
        all_signals.append(list2)

index_1 = 1
index_2 = 2  # One extra, because [[2]] comes before [[6]]
for s in all_signals:
    if recurse_greater([[2]], s) > 0:
        index_1 += 1
    if recurse_greater([[6]], s) > 0:
        index_2 += 1
print(index_1 * index_2)
