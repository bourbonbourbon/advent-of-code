import re

def parse(line):
    blue = [int(j) for j in re.findall(r"(\d*) blue", line)]
    red = [int(j) for j in re.findall(r"(\d*) red", line)]
    green = [int(j) for j in re.findall(r"(\d*) green", line)]
    return max(blue), max(red), max(green)


with open("input.txt", "r") as file:
    total = 0
    for line in file:
        blue, red, green = parse(line)
        total += blue * red * green
    print(total)
