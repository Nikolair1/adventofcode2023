import re

sum = 0
f = open("input.txt", "r")
for line in f:
    digits = re.findall(r"\d", line)
    if digits:
        sum += int(digits[0] + digits[-1])
print(sum)
