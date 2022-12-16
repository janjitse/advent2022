import sys
import re
from typing import List, Tuple
from functools import lru_cache


class Valve:
    def __init__(self, connections: List["Valve"], flow_rate: int, name: str):
        self.connections = connections.copy()
        self.flow_rate = flow_rate
        self.name = name


valve_dict = {}
connection_dict = {}
visited_dict = {}
opened_dict = {}
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        name = line[len("Valve ") : len("Valve AA")]
        flow_rate = int(re.findall(r"(\d+)", line)[0])
        connections = re.findall(r"([A-Z]{2})", line)[1:]
        valve_dict[name] = Valve(connections=[], flow_rate=flow_rate, name=name)
        connection_dict[name] = connections
        visited_dict[name] = {c: False for c in connections}
        opened_dict[name] = False

opened_list = [False] * len(opened_dict)
valve_name_index = {}
for i, name in enumerate(valve_dict):
    valve_name_index[name] = i
    if valve_dict[name].flow_rate == 0:
        opened_list[i] = True
opened_tuple = tuple(opened_list)


for valve in valve_dict.values():
    for conn in connection_dict[valve.name]:
        valve.connections.append(valve_dict[conn])

max_time = 30


@lru_cache(maxsize=None)
def recurse(time_left: int, cur_node: str, opened: Tuple[bool, ...]) -> int:
    if time_left < 0:
        return 0
    if all(opened):
        return 0
    return_flow = 0
    for conn in valve_dict[cur_node].connections:
        return_flow = max([return_flow, recurse(time_left - 1, conn.name, opened)])
    cur_index = valve_name_index[cur_node]
    if not opened[cur_index]:
        new_opened = opened[:cur_index] + (True,) + opened[cur_index + 1 :]
        add_flow = valve_dict[cur_node].flow_rate * (time_left - 1)
        return_flow = max(
            [return_flow, recurse(time_left - 1, cur_node, new_opened) + add_flow]
        )
    return return_flow


print(recurse(max_time, "AA", opened_tuple))
