import re

f = open("input.txt", "r")
sum = 0

for line in f:
    split = re.split(r";", line)
    max_b, max_g, max_r = 0, 0, 0
    for round in split:
        blue_match = re.search("(?=\d+\sblue)\d+", round)
        green_match = re.search("(?=\d+\sgreen)\d+", round)
        red_match = re.search("(?=\d+\sred)\d+", round)
        if blue_match:
            max_b = max(int(blue_match.group(0)), max_b)
        if green_match:
            max_g = max(int(green_match.group(0)), max_g)
        if red_match:
            max_r = max(int(red_match.group(0)), max_r)
    sum += max_r * max_g * max_b

print(sum)
