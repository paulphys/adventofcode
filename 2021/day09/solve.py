data = [x.strip() for x in open("input.txt")]
adjacent = [(-1, 0), (1, 0),  # top, bottom
            (0, -1), (0, 1)]  # left, right
checked = {}

def adj(row, col):
    pos = []
    for z in adjacent:
        y, x = (row + z[0], col + z[1])
        if y < 0 or x < 0 or y > 99 or x > 99:
            continue
        pos.append((y, x))
    return pos

def minima():
    points = []
    for y in range(len(data)):
        for x in range((len(data[0]))):
            values = []
            for row, col in adj(y, x):
                values += [int(data[row][col])]
            v = int(data[y][x])
            if min(values) > v:
                points.append((y, x))
    return points

def basin(y, x):
    points = [(y, x)]
    checked[(y, x)] = 1
    for row, col in adj(y, x):
        if (row, col) in checked or int(data[row][col]) >= 9:
            continue
        points += basin(row, col)
    return points

def part1():
    risk = 0
    for y, x in minima():
        risk += int(data[y][x]) + 1
    return risk

def part2():
    basins = []
    for y, x in minima():
        basins.append(set(basin(y, x)))
    size = sorted([len(x) for x in basins], reverse=True)
    return size[0] * size[1] * size[2]

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
