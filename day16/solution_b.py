import sys
import itertools
import re
from functools import lru_cache
from typing import List, Tuple

connection_dict = {}
flow_rate_dict = {}
valve_list = []
valve_index = {}

j = 0

with open(sys.path[0] + "/input.txt", "r") as f:
    for i, line in enumerate(f):
        name = line[len("Valve ") : len("Valve AA")]
        flow_rate = int(re.findall(r"(\d+)", line)[0])
        connections = re.findall(r"([A-Z]{2})", line)[1:]
        connection_dict[name] = connections
        if flow_rate > 0:
            valve_list.append(name)
            flow_rate_dict[name] = flow_rate
            valve_index[name] = j
            j += 1

flow_relieved = dict()
nr_relieve = len(valve_list)
for opens in itertools.product([True, False], repeat=nr_relieve):
    flow_opens = sum([flow_rate_dict[n] for i, n in enumerate(valve_list) if opens[i]])
    flow_relieved[tuple(opens)] = flow_opens


# @lru_cache(maxsize=None)
def possible_next(
    location_1: str, location_2: str, opens: Tuple[bool, ...]
) -> List[Tuple[str, str, Tuple[bool, ...]]]:
    possible = []
    moves = just_move(location_1, location_2)
    for c_1, c_2 in moves:
        possible.append((c_1, c_2, opens))
    for open_loc, move_loc in [(location_1, location_2), (location_2, location_1)]:
        if open_loc in valve_index:
            open_index = valve_index[open_loc]
            if not opens[open_index]:
                new_opens = opens[:open_index] + (True,) + opens[open_index + 1 :]
                for c_2 in connection_dict[move_loc]:
                    possible.append((min(open_loc, c_2), max(open_loc, c_2), new_opens))
        if open_loc == move_loc:  # only run once if they're both at the same location
            break
    if (
        location_1 != location_2
        and location_1 in valve_index
        and location_2 in valve_index
    ):
        index_1 = valve_index[location_1]
        index_2 = valve_index[location_2]
        if not opens[index_1] and not opens[index_2]:
            new_opens_l = list(opens)
            new_opens_l[index_1] = True
            new_opens_l[index_2] = True
            new_opens = tuple(new_opens_l)
            possible.append((location_1, location_2, new_opens))
    return possible


@lru_cache(maxsize=None)
def just_move(location_1: str, location_2: str) -> List[Tuple[str, str]]:
    possible_moves = []
    for c_1 in connection_dict[location_1]:
        for c_2 in connection_dict[location_2]:
            possible_moves.append((min(c_1, c_2), max(c_1, c_2)))
    return possible_moves


initial_flow_states = tuple([False] * nr_relieve)
states = dict()
states[("AA", "AA", initial_flow_states)] = 0
for time in range(20):
    print(f"time {time}")
    next_states = states.copy()
    for loc_1, loc_2, opens in states:
        cur_max = states[(loc_1, loc_2, opens)] + flow_relieved[opens]
        if all(opens):
            for l_1, l_2 in just_move(loc_1, loc_2):
                next_states[(l_1, l_2, opens)] = max(
                    next_states.get((l_1, l_2, opens), 0), cur_max
                )
        for l_1, l_2, new_opens in possible_next(loc_1, loc_2, opens):
            next_states[(l_1, l_2, new_opens)] = max(
                next_states.get((l_1, l_2, new_opens), 0),
                cur_max,
            )

    states = next_states
print(max(states.values()))
