import re
import sys

operator_dict = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
}

monkey_dict = {}


class Monkey:
    def __init__(self, operator, name, children_n=None, value=None):
        self.name = name
        self.operator = operator
        self.children_n = children_n
        self._value = value
        self.parent = None

    def calc_value(self):
        a1 = self.children[0].value()
        a2 = self.children[1].value()
        self._value = operator_dict[self.operator](a1, a2)
        return self._value

    def value(self):
        if self._value is not None:
            return self._value
        else:
            if self.children:
                a1 = self.children[0].value()
                a2 = self.children[1].value()
                self._value = operator_dict[self.operator](a1, a2)
                return self._value

    def update(self, new_value):
        self._value = new_value
        if self.parent:
            new_parent_value = self.parent.calc_value()
            self.parent.update(new_parent_value)


with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        name, col_split = line.strip().split(":")
        numbers = re.findall(r"(\d+)", col_split)
        if len(numbers) > 0:
            value = int(numbers[0])
            operator = None
            children = None
        else:
            child1, operator, child2 = col_split.strip().split(" ")
            value = None
            children = [child1, child2]
        monkey = Monkey(operator, name, children, value)
        monkey_dict[name] = monkey

for monkey in monkey_dict.values():
    if monkey.children_n:
        monkey.children = [
            monkey_dict[monkey.children_n[0]],
            monkey_dict[monkey.children_n[1]],
        ]
        if monkey.children[0].parent or monkey.children[1].parent:
            print("Parent alreay exists")
        monkey.children[0].parent = monkey
        monkey.children[1].parent = monkey
print(monkey_dict["root"].value())

cur_monkey = monkey_dict["humn"]
while cur_monkey.parent:
    # print(cur_monkey.operator)
    print()
    if cur_monkey.children_n:
        print(
            cur_monkey.value(),
            cur_monkey.children[0].value(),
            cur_monkey.operator,
            cur_monkey.children[1].value(),
        )
    cur_monkey = cur_monkey.parent

prev_value = 0
attempt = 1
prev_attempt = 1
# check = 5497558138879
# monkey_dict["humn"].update(check)
# print(monkey_dict["root"].children[0].value())
# print(monkey_dict["root"].children[1].value())
while True:
    print(attempt)
    child1 = monkey_dict["root"].children[0]
    child2 = monkey_dict["root"].children[1]
    monkey_dict["humn"].update(attempt)
    if child1.value() == child2.value():
        print(attempt)
        break
    if child1.value() > child2.value():
        prev_attempt = attempt
        attempt *= 2
    else:
        break
    # if child1.value() < child2.value():
    #     tmp_attempt = attempt
    #     attempt = (attempt - prev_attempt) // 2 + prev_attempt
    #     prev_attempt = tmp_attempt
search_max = attempt
prev_attempt = 0
attempt = search_max // 2
while True:
    print(attempt)
    child1 = monkey_dict["root"].children[0]
    child2 = monkey_dict["root"].children[1]
    monkey_dict["humn"].update(attempt)
    if abs(attempt - prev_attempt) < 1:
        print(f"Search too small")
        print(child1.value())
        print(child2.value())
        break
    if child1.value() == child2.value():
        print(f" found: {attempt}")
        for i in range(4):
            monkey_dict["humn"].update(attempt - i)
            print(child1.value())
        print(child2.value())
        break
    if child1.value() > child2.value():
        tmp_attempt = attempt
        attempt = attempt + abs(attempt - prev_attempt + 1) // 2
        prev_attempt = tmp_attempt
    else:
        tmp_attempt = attempt
        attempt = attempt - abs(attempt - prev_attempt + 1) // 2
        prev_attempt = tmp_attempt
