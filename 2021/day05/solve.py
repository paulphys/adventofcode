with open('input.txt','r') as input:
    data = [[[int(y) for y in x.split(',')] for x in line.strip('\n').split(' -> ')] for line in input]

def hydro(part):
    position = {}
    for coordinates in data:
        start, end = coordinates
        x1,y1 = start[0],start[1]
        x2,y2 = end[0],end[1]

        if x1 != x2 and y1 != y2:
            if part == 1: continue
        if x1 < x2:
            xstep = 1
        elif x1 > x2:
            xstep = -1
        else: xstep = 0
        if y1 < y2:
            ystep = 1
        elif y1 > y2:
            ystep = -1
        else: ystep = 0

        start = (x1, y1)
        position[start] = position.get(start, 0) + 1
        while x1 != x2 or y1 != y2:
            x1 += xstep
            y1 += ystep
            start = (x1, y1)
            position[start] = position.get(start, 0) + 1
    overlap = len(list(filter(lambda x: position[x] > 1, position)))
    return overlap

print(f"Part 1: ", hydro(1))
print(f"Part 2: ", hydro(2))
