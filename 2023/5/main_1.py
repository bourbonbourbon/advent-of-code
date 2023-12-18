import re

def parse_numbers(line):
    nums_re = re.compile("(\d+)")
    return [int(match) for match in nums_re.findall(line)]

def map_gen(name, index):
    r = re.compile(rf"{name}{maps_re}")
    values = r.search(data)
    l = []
    for line in values.group(1).strip().split("\n"):
        destination, source, steps = parse_numbers(line)
        if index == 0:
            c = seeds
        else:
            # getting the "y" coordinate of previous map
            c = [x[1] for x in maps[index - 1]]
        for _, num in enumerate(c):
            if num >= source and num < source + steps:
                diff = num - source
                l.append((num, destination + diff))
    # checking for any sources to destination does not exist
    c2 = [x[0] for x in l]
    for num in c:
        if num not in c2:
            l.append((num, num))
    return l

def solve_seeds(maps):
    seed_location = {}
    for seed in seeds:
        val = seed
        for map in maps:
            nums = [x[0] for x in map]
            index = nums.index(val)
            val = map[index][1]
        seed_location[seed] = val
        seed_location = dict(
            sorted(seed_location.items(), key=lambda item: item[1]))
    print(list(seed_location.values())[0])


with open("input.txt", "r") as file:
    data = file.read()

seeds = []
maps = []

uni_re = "((?:\d+\s)+)"

seeds_re = re.compile(rf"seeds: {uni_re}")
seeds = parse_numbers(*seeds_re.findall(data))

maps_re = f" map:\n{uni_re}"
map_names = ["seed-to-soil", "soil-to-fertilizer",
             "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

for index, name in enumerate(map_names):
    maps.append(map_gen(name, index))

solve_seeds(maps)
