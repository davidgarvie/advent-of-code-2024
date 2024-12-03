import re

f = open("input.txt", "r")
data = f.read()

matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)
total = 0

enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            l,r = map(int, match[4:-1].split(","))
            total += l * r

print(f"The total is: {total}")