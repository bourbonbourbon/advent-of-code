import re

with open("input.txt", "r") as file:
    data = [[line.strip()] for line in file]

w = re.compile(r"(\d+)")

total = 0

for row in data:
    card_total = 0
    wining = [int(m.group(1)) for m in w.finditer(row[0].split("|")[0].split(":")[1])]
    numbers = [int(m.group(1)) for m in w.finditer(row[0].split("|")[1])]

    for num in numbers:
        if num in wining:
            if card_total == 0:
                card_total += 1
            else:
                card_total *= 2
    total += card_total
print(total)
