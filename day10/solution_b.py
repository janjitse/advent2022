import sys

cycles = 0
var_x = 1

crt = []

with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        instruction = l.strip().split(" ")
        if cycles % 40 == 0:
            crt.append([])
            cycles = cycles % 40
        if abs(var_x - cycles) <= 1:
            crt[-1].append("#")
        else:
            crt[-1].append(".")
        cycles += 1

        if instruction[0] == "addx":
            if cycles % 40 == 0:
                crt.append([])
                cycles = cycles % 40
            if abs(var_x - cycles) <= 1:
                crt[-1].append("#")
            else:
                crt[-1].append(".")
            cycles += 1
            var_x += int(instruction[1])

for l in crt:
    print("".join(l))
