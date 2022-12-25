import sys

trans_dict = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def snafu_to_nr(string):
    max_value = len(string) - 1
    snafu = 0
    for i, c in enumerate(string):
        snafu += pow(5, max_value - i) * trans_dict[c]
    return snafu


snafu_values = []
with open(sys.path[0] + "/input.txt", "r") as f:
    for line in f:
        snafu_values.append(snafu_to_nr(line.strip()))

print(snafu_values)
total_value = sum(snafu_values)
length = 0
while pow(5, length) < total_value:
    length += 1

output = ""
remaining_value = total_value
retrans_dict = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
for rem_length in range(length + 1, -1, -1):
    for rem in range(-2, 3):
        max_possible = rem * pow(5, rem_length) + sum(
            [2 * pow(5, i) for i in range(rem_length)]
        )

        if max_possible >= remaining_value:
            output += retrans_dict[rem]
            remaining_value -= rem * pow(5, rem_length)
            break

print(total_value)
print(snafu_to_nr(output))
print(output.lstrip("0"))
