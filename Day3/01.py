import string
import re

f = open("input.txt", "r")
result = 0

all_symbols = [
    char
    for char in string.printable
    if char.isascii() and not char.isalnum() and char != "."
]

lines = f.read().splitlines()
n = len(lines)
m = len(lines[0])


def symbol_checker(numbers, row):
    global result

    for number in numbers:
        left, right = number
        found_symbol = False

        for i in range(row - 1, row + 2):
            for j in range(left - 1, right + 1):
                if i >= 0 and i < n and j >= 0 and j < m:
                    if lines[i][j] in all_symbols:
                        temp = "".join(lines[row][left:right])
                        print(temp)
                        result += int(temp)
                        found_symbol = True
                        break
            if found_symbol:
                break


for index, line in enumerate(lines):
    matches = [(match.start(), match.end()) for match in re.finditer("\d+", line)]
    symbol_checker(matches, index)


print(result)
