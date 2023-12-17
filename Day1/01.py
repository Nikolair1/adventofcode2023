import re

sum = 0
f = open("input.txt", "r")
o = open("o_1.txt", "w")
for line in f:
    digits = re.findall(r"\d", line)
    if digits:
        sum += int(digits[0] + digits[-1])
o.write(str(sum))
