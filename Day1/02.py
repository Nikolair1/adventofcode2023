import re


def convert_value(value):
    match value:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(value)


sum = 0
f = open("input.txt", "r")
o = open("o_2.txt", "w")

for line in f:
    digits = re.findall(
        "(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))", line
    )
    if digits:
        sum += 10 * convert_value(digits[0]) + convert_value(digits[-1])

o.write(str(sum))
