# Part 1

def solution():
    pointing = 50
    zeros = 0

    f = open("advent_of_code_2025/day_1/input.txt", "r")
    for line in f:
        if line[0] == "L":
            pointing -= int(line[1:])
        elif line[0] == "R":
            pointing += int(line[1:])

        pointing %= 100

        if (pointing == 0):
            zeros += 1

    return zeros

print(solution())
