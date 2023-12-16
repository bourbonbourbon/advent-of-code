# https://www.reddit.com/r/adventofcode/comments/189m3qw/comment/kbs55ge/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import re
from collections import defaultdict
from math import prod

with open("data") as f:
    lines = f.read().split("\n")

# building symbols grid as {xy_position: symbol}
symbols = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            symbols[(x, y)] = c

# checking if a number has a rectangular neighborhood containing a symbol and
# building a gear grid as {gear_position: [part numbers list]}
gears = defaultdict(list)
part_numbers_sum = 0
for y, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        for (s_x, s_y), c in symbols.items():
            if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                num = int(match.group())
                part_numbers_sum += num
                if c == "*":
                    gears[(s_x, s_y)].append(num)
                break

# ========= PART 1 =========
print(part_numbers_sum)

# ========= PART 2 =========
print(sum(prod(part_nums)
      for part_nums in gears.values() if len(part_nums) == 2))
