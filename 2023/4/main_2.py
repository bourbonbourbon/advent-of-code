import re

with open("input.txt", "r") as file:
    data = [[line.strip()] for line in file]

w = re.compile(r"(\d+)")

no_of_cards = len(data)
instances = [1] * no_of_cards

for row in data:
    matches = 0
    wining = [int(m.group(1))
              for m in w.finditer(row[0].split("|")[0].split(":")[1])]
    numbers = [int(m.group(1)) for m in w.finditer(row[0].split("|")[1])]
    card_no = int(row[0].split("|")[0].split(":")[0].split()[1])

    for num in numbers:
        if num in wining:
            matches += 1
    
    if matches != 0:
        for i in range(matches):
            instances[card_no + i] += instances[card_no - 1]

print(sum(instances))

# each card has one instance
# find no of matches
    # select those many cards
    # create X_instance number of copies
