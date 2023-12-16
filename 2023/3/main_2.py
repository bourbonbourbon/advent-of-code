import re

def builder(line):
    l = []
    for m in num_re.finditer(line):
        l.append((m.start(), m.end(), int(m.group(1))))
    return l


def check_matrix(star, numbers):
    matched_nums = []
    for number in numbers: # three lists
        for l in number:
            if (l[0] - 1 == star[0]) or (l[0] == star[0]) or (l[0] + 1 == star[0]) or (l[1] - 1 == star[1]) or (l[1] == star[1]) or (l[1] + 1 == star[1]):
                matched_nums.append(l[2])
    if len(matched_nums) == 2:
        return matched_nums[0] * matched_nums[1]
    return 0


with open("input.txt", "r") as file:
    data = [[line.strip()] for line in file]

last_row = len(data)

num_re = re.compile(r"(\d+)")
star_re = re.compile(r"[*]")
total = 0
for i in range(1, last_row - 1):
    for match in star_re.finditer(*data[i]):
        numbers = [builder(*data[i - 1]),
                   builder(*data[i]), builder(*data[i + 1])]
        total += check_matrix(star=(match.start(), match.end()), numbers=numbers)

print(total)
