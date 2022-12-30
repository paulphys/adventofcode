data = set(line.strip() for line in open("input.txt"))
p = 0

mask = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

for x, y, z in data:
    p += 6
    for dx, dy, dz in mask:
        if (x+dx, y+dy, z+dz) in data:
            p -= 1

print(p)
