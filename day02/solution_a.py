import sys

score_dict = {
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("A", "Z"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
    ("C", "Z"): 3 + 3,
}
guide = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for l in f:
        guide.append(tuple(l.strip().split()))

score = 0
for g in guide:
    score += score_dict[g]
print(score)

score_dict_b = {
    ("A", "X"): 3 + 0,
    ("A", "Y"): 1 + 3,
    ("A", "Z"): 2 + 6,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 2 + 0,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 1 + 6,
}
score_b = 0
for g in guide:
    score_b += score_dict_b[g]
print(score_b)
