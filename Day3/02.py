import re

f = open("input.txt", "r")
result = 0


lines = f.read().splitlines()
n = len(lines)
m = len(lines[0])


def gear_check(stars, row):
    global result

    for star in stars:
        numbers_found = []
        # First let's check the row above
        if row - 1 >= 0:
            middle = star
            left = star - 1
            right = star + 1
            while left >= 0 and lines[row - 1][left].isdigit():
                left -= 1
            while right < m and lines[row - 1][right].isdigit():
                right += 1
            if lines[row - 1][middle].isdigit():
                numbers_found.append(lines[row - 1][left + 1 : right])
            else:
                if left < star - 1:
                    numbers_found.append(lines[row - 1][left + 1 : middle])

                if right > star + 1:
                    numbers_found.append(lines[row - 1][middle + 1 : right])
        # Next the sides
        left = star - 1
        while left >= 0 and lines[row][left].isdigit():
            left -= 1
        if left < star - 1:
            numbers_found.append(lines[row][left + 1 : star])
        right = star + 1
        while right < m and lines[row][right].isdigit():
            right += 1
        if right > star + 1:
            numbers_found.append(lines[row][star + 1 : right])
        # Bottom
        if row + 1 < n:
            middle = star
            left = star - 1
            right = star + 1
            while left >= 0 and lines[row + 1][left].isdigit():
                left -= 1
            while right < m and lines[row + 1][right].isdigit():
                right += 1
            if lines[row + 1][middle].isdigit():
                numbers_found.append(lines[row + 1][left + 1 : right])
            else:
                if left < star - 1:
                    numbers_found.append(lines[row + 1][left + 1 : middle])

                if right > star + 1:
                    numbers_found.append(lines[row + 1][middle + 1 : right])

        if len(numbers_found) == 2:
            result += int(numbers_found[0]) * int(numbers_found[1])


"""
34#45
##*##
#####
"""


for index, line in enumerate(lines):
    matches = [match.start() for match in re.finditer("\*", line)]
    gear_check(matches, index)


print(result)
