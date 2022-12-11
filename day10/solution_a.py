import sys

instr_cycle = {"addx": 2, "noop": 1}
cycles = 1
var_x = 1
signal_strength = 0
to_add = [20, 60, 100, 140, 180, 220]
with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        instruction = l.strip().split(" ")

        cycles += 1
        if cycles in to_add:
            print(var_x)
            signal_strength += cycles * var_x
        if instruction[0] == "addx":
            var_x += int(instruction[1])
            cycles += 1
            if cycles in to_add:
                print(var_x)
                signal_strength += cycles * var_x

print(signal_strength)
