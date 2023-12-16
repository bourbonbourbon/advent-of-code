# https://www.reddit.com/r/adventofcode/comments/1883ibu/comment/kbj2stu/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import re

with open("input.txt") as f:
    data = f.read().strip()


def calibration(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)


# Part 1
print(calibration(data))

# Part 2
data = (
    data.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "f4r")
    .replace("five", "f5e")
    .replace("six", "s6x")
    .replace("seven", "s7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e")
)
print(calibration(data))
