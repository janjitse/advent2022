import sys

from utils import stupid_parser, recurse_greater


right_index = 0

with open(sys.path[0] + "/input.txt", "r") as f:
    signals = f.read().strip().split("\n\n")
    for i, signal in enumerate(signals, 1):
        s1, s2 = signal.split("\n")
        list1 = stupid_parser(s1)
        list2 = stupid_parser(s2)
        if recurse_greater(list1, list2) < 0:
            right_index += i

print(right_index)
