# range (a, b)
# if a > b then range(b, a)[::-1] reverse


maps = [
    [(79, 93), (55, 68)],
    [(81, 95), (57, 70)],
    [(81, 95), (57, 70)],
    [(81, 95), (53, 62)],
    [(74, 88), (46, 55)],
    [(78, 56), (82, 91)],
    [(78, 56), (82, 91)],
    [(82, 60), (86, 96)],
]

for map in maps:
    for s in map:
        if s[0] > s[1]:
            print(list(range(s[0]-s[1]+(((s[0]-s[1])//10)*10) + 1, s[0])), end="")
        else:
            print(list(range(s[0], s[1])), end="")
    print()

