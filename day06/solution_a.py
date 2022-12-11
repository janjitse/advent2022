import sys

with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        for i in range(len(l.strip())):
            if len(set(list(l[i : i + 14]))) == 14:
                print(i + 14)
                break
