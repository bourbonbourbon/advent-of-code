import re

BLUE = 14
RED = 12
GREEN = 13

def parse(line):
    game_no = int(line.split(":")[0].split(" ")[1])
    blue = [int(j) for j in re.findall(r"(\d*) blue", line)]
    red = [int(j) for j in re.findall(r"(\d*) red", line)]
    green = [int(j) for j in re.findall(r"(\d*) green", line)]
    return game_no, max(blue), max(red), max(green)


with open("input.txt", "r") as file:
    total = 0
    for line in file:
        game_no, blue, red, green = parse(line)
        if blue <= BLUE and red <= RED and green <= GREEN:
            total += game_no
    print(total)
