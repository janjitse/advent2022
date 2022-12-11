import sys

with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        for i in range(len(line.strip())):
            if len(set(list(line[i : i + 14]))) == 14:
                print(i + 14)
                break
