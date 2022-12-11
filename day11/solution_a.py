from operator import add, mul
from functools import reduce
from collections import OrderedDict
from typing import Callable, List
import re
import sys


class Monkey:
    def __init__(
        self,
        name: str,
        items: List[int],
        operation: Callable[[int, int], int],
        add: int,
        divisor: int,
        true_cond,
        false_cond,
    ):
        # self.name = name
        self.items = items.copy()
        self._operator = operation
        self._add = add
        self._divisor = divisor
        self.true_condition = true_cond
        self.false_condition = false_cond
        self.items_inspected = 0

    def operation(self, worry_level):
        if self._add.strip() == "old":
            return self._operator(worry_level, worry_level)
        else:
            return self._operator(worry_level, int(self._add))

    def check_op(self, worry_level):
        self.items_inspected += 1

        return worry_level % self._divisor == 0


with open(sys.path[0] + "/input.txt", "r") as f:
    total = f.read()

monkey_strings = total.split("\n\n")

op_dict = {"+": add, "*": mul}

monkeys = OrderedDict()

all_divisors = []

for monkey in monkey_strings:
    monkey = monkey.split("\n")
    name = monkey[0].strip().lower()[:-1]
    items = [int(d) for d in re.findall("\d+", monkey[1])]
    op = re.findall("\*|\+", monkey[2])[0]
    number = monkey[2].split(op)[1]
    divisor = int(re.findall("\d+", monkey[3])[0])
    all_divisors.append(divisor)
    true_cond = re.findall("monkey \d+", monkey[4])[0]
    false_cond = re.findall("monkey \d+", monkey[5])[0]
    monkeys[name] = Monkey(
        name=name,
        items=items,
        operation=op_dict[op],
        add=number,
        divisor=divisor,
        true_cond=true_cond,
        false_cond=false_cond,
    )
worry_level = 0

lcm = reduce(lambda x, y: x * y, all_divisors)
for round in range(10_000):
    for m in monkeys.values():
        while m.items:
            i = m.items.pop(0)
            worry_level = m.operation(i)
            # worry_level //= 3
            cond = m.check_op(worry_level)
            worry_level = worry_level % lcm
            if cond:
                monkeys[m.true_condition].items.append(worry_level)
            else:
                monkeys[m.false_condition].items.append(worry_level)

inspected_list = sorted([m.items_inspected for m in monkeys.values()])
print(inspected_list[-1] * inspected_list[-2])
