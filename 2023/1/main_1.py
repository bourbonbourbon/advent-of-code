file = open("input.txt", "r")

total = 0

for line in file:
    first_num = 0
    last_num = 0
    for char in line:
        if char.isdigit():
            if first_num == 0:
                first_num = last_num = int(char)
            last_num = int(char)
    number = first_num * 10 + last_num
    total += number

print(total)
file.close()
