from __future__ import annotations
import sys
from typing import List, Optional


class Node:
    def __init__(
        self, value: int, left: Optional[Node] = None, right: Optional[Node] = None
    ):
        self.value = value
        self.left = left
        self.right = right


with open(sys.path[0] + "/input.txt", "r") as f:
    numbers = [int(b) for b in f.read().strip().split("\n")]

queue: List[Node] = []
key = 811589153
# key = 1
nr_iterations = 10
for i, n in enumerate(numbers):
    if i > 0:
        node = Node(n * key, left=queue[-1])
        queue[-1].right = node
    if i == 0:
        node = Node(n * key)
    queue.append(node)

queue[0].left = queue[-1]
queue[-1].right = queue[0]
queue_length = len(queue)


def print_queue(queue: List[Node], start_index: int = 0) -> None:
    to_print = []
    start = queue[start_index]
    for _ in range(len(queue)):
        to_print.append(start.value)
        start = start.right
    print(to_print)


for i in range(nr_iterations):
    for node in queue:
        to_move = node.value % (queue_length - 1)
        orig_right = node.right
        orig_left = node.left
        if to_move != 0:
            node.left.right = orig_right
            node.right.left = orig_left
        if to_move > 0:
            right = orig_right
            for _ in range(to_move):
                right = right.right
            node.right = right
            node.left = right.left
            right.left = node
            node.left.right = node

for i, node in enumerate(queue):
    if node.value == 0:
        zero_index = i
node_c = queue[zero_index]

one_value = 0
two_value = 0
three_value = 0
for i in range(3001):
    if i == 1000:
        one_value = node_c.value
    elif i == 2000:
        two_value = node_c.value
    elif i == 3000:
        three_value = node_c.value
    node_c = node_c.right

print(one_value, two_value, three_value)
print(one_value + two_value + three_value)
