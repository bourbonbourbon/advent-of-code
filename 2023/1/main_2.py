num_list = ["one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]


def check_word(word_list, first_num, last_num):
    for i in range(len(word_list)):
        if word_list[i] in num_list:
            if first_num == 0:
                first_num = last_num = num_list.index(word_list[i]) + 1
            last_num = num_list.index(word_list[i]) + 1
            break

    return first_num, last_num


def main():
    file = open("input.txt", "r")
    total = 0

    for line in file:
        first_num = 0
        last_num = 0
        i = 0

        while i < len(line) - 1:
            if line[i].isdigit():
                if first_num == 0:
                    first_num = last_num = int(line[i])
                last_num = int(line[i])

            else:
                word_list = []
                word_list.append(line[i: i + 3:])
                word_list.append(line[i: i + 4:])
                word_list.append(line[i: i + 5:])
                first_num, last_num = check_word(
                    word_list, first_num, last_num)

            i += 1

        number = first_num * 10 + last_num
        total += number

    print(total)
    file.close()


main()
