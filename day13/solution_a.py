import sys
from typing import Any, List, Union


def recurse_greater(list1: Union[int, List[Any]], list2: Union[int, List[Any]]) -> int:
    if type(list1) == int and type(list2) == int:
        if list1 > list2:
            return 1
        elif list1 == list2:
            return 0
        else:
            return -1
    if type(list1) == int:
        list1 = [list1]
    if type(list2) == int:
        list2 = [list2]
    assert type(list1) == list and type(list2) == list
    for l1, l2 in zip(list1, list2):
        outcome = recurse_greater(l1, l2)
        if outcome > 0:
            return 1
        elif outcome < 0:
            return -1
    if len(list1) < len(list2):
        return -1
    if len(list1) > len(list2):
        return 1
    return 0


def stupid_parser(input_str: str) -> List[Any]:
    depth = 0
    output_list = []
    digits = ""
    start = 0
    for i, c in enumerate(input_str[1:], 1):
        if c == "[":
            if depth == 0:
                start = i
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                f = stupid_parser(input_str[start:i])
                output_list.append(f)
        elif c == ",":
            if len(digits) > 0:
                output_list.append(int(digits))
                digits = ""
        elif depth == 0:
            digits += c
    if len(digits) > 0:
        output_list.append(int(digits))
    return output_list


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
