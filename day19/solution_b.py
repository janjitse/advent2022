import re
import sys
from typing import NamedTuple
from collections import deque
from multiprocessing import Process


class Costs(NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0


class Blueprints(NamedTuple):
    ore: Costs
    clay: Costs
    obsidian: Costs
    geode: Costs


blueprints = {}
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        blueprints_parsed = [int(d) for d in re.findall(r"(\d+)", line)]
        blueprints[blueprints_parsed[0]] = Blueprints(
            ore=Costs(ore=blueprints_parsed[1]),
            clay=Costs(ore=blueprints_parsed[2]),
            obsidian=Costs(ore=blueprints_parsed[3], clay=blueprints_parsed[4]),
            geode=Costs(ore=blueprints_parsed[5], obsidian=blueprints_parsed[6]),
        )


def task(bp_id):
    blueprint = blueprints[bp_id]
    max_cost = [-1] * 4
    for i in range(3):
        max_cost[i] = max([blueprint[c][i] for c in range(4) if c != i])

    queue = deque()
    queue.append([1, 0, 0, 0, 32, 0, 0, 0, 0])
    max_geode = 0
    while queue:
        state = queue.pop()
        if state[4] == 1:
            max_geode = max(max_geode, state[8] + state[3])
            continue
        if max_geode > state[8] + state[3] * state[4] + sum(
            [i for i in range(1, state[4])]
        ):
            continue
        new_state = state.copy()
        for robot_i in range(4):
            new_state[5 + robot_i] += new_state[robot_i]
        new_state[4] -= 1
        for robot_i in range(4):
            if state[4] == 2 and robot_i != 3:
                continue
            if robot_i < 3 and state[robot_i] * state[4] + new_state[
                robot_i + 5
            ] >= max_cost[robot_i] * (state[4] - 2):
                continue
            else:
                possible = True
                for res_j in range(3):
                    if blueprint[robot_i][res_j] > state[5 + res_j]:
                        possible = False
                        break
                if possible:
                    robot_state = new_state.copy()
                    robot_state[robot_i] += 1
                    for res_j in range(3):
                        robot_state[5 + res_j] -= blueprint[robot_i][res_j]
                    queue.append(robot_state)
        queue.append(new_state)

    print(bp_id, max_geode)


for bp_id in range(1, 3):
    process = Process(target=task, args=(bp_id,))
    process.start()
