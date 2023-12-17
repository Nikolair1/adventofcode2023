import re

f = open("input.txt", "r")
sum = 0

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

for line in f:
    split = re.split(r";", line)
    colon = split[0].find(":")
    id = split[0][5:colon]
    valid = True
    for round in split:
        blue_match = re.search("(?=\d+\sblue)\d+", round)
        green_match = re.search("(?=\d+\sgreen)\d+", round)
        red_match = re.search("(?=\d+\sred)\d+", round)
        if blue_match:
            if int(blue_match.group(0)) > BLUE_CUBES:
                valid = False
                break
        if green_match:
            if int(green_match.group(0)) > GREEN_CUBES:
                valid = False
                break
        if red_match:
            if int(red_match.group(0)) > RED_CUBES:
                valid = False
                break
    if valid:
        sum += int(id)

print(sum)
