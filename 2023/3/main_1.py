import re


def check_index(row, col):
    try:
        if data[row][0][col] not in check_list:
            return True
    except IndexError:
        pass
    return False


def check_matrix(start, end, number, row):
    # top
    if row != 0:
        i = start
        while i < end:
            if check_index(row - 1, i):
                return number
            i += 1
        # top left diagonal
        if start != 0 and check_index(row - 1, start - 1):
            return number
        # top right diagonal
        if end != 139 and check_index(row - 1, end):
            return number

    # bottom
    if row != last_row:
        i = start
        while i < end:
            if check_index(row + 1, i):
                return number
            i += 1
        # bottom left diagonal
        if start != 0 and check_index(row + 1, start - 1):
            return number
        # bottom right diagonal
        if end != 139 and check_index(row + 1, end):
            return number

# edges
# left
    # adj
    if start != 0 and check_index(row, start - 1):
        return number

# right
    # adj
    if end != 139 and check_index(row, end):
        return number

    return 0


with open("input.txt", "r") as file:
    data = [[line.strip()] for line in file]

line_len = len(*data[0])
last_row = len(data)
check_list = list(range(10)) + [".", "\n"]

p = re.compile(r"(\d+)")
total = 0
for i in range(last_row):
    for match in p.finditer(data[i][0]):
        start, end = match.span()
        total += check_matrix(start, end, int(match.group(0)), i)

print(total)
