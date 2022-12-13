from typing import Any, List, Union


def sign(a: int, b: int) -> int:
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0


def recurse_greater(list1: Union[int, List[Any]], list2: Union[int, List[Any]]) -> int:
    if type(list1) == int and type(list2) == int:
        return sign(list1, list2)
    if type(list1) == int:
        list1 = [list1]
    if type(list2) == int:
        list2 = [list2]
    assert type(list1) == list and type(list2) == list
    for l1, l2 in zip(list1, list2):
        outcome = recurse_greater(l1, l2)
        if outcome != 0:
            return outcome
    return sign(len(list1), len(list2))


def stupid_parser(input_str: str) -> List[Any]:
    depth = 0
    output_list = []
    digits = ""
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
        elif c == "," and len(digits) > 0:
            output_list.append(int(digits))
            digits = ""
        elif depth == 0 and c in "0123456789":
            digits += c
    if len(digits) > 0:
        output_list.append(int(digits))
    return output_list
