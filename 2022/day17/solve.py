from itertools import cycle
from collections import defaultdict

jets = cycle(open("input.txt").read().strip())
left, right = "<", ">"
jetdir = {left: -1, right: 1}

rocks = cycle((
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),))

def tlx(rock, dx):
    for idx in range(len(rock)):
        rock[idx][0] += dx

def tly(rock, dy):
    for idx in range(len(rock)):
        rock[idx][1] += dy

def checkwalls(rock, dx):
    for p in rock:
        if not (0 <= p[0]+dx <= 6):
            return False
    return True

def checkblock(rock, v, dx, dy):
    for x, y in rock:
        if (x+dx, y+dy) in v:
            return False
    return True

def prune(v, top):
    for p in [p for p in v if p[1] < top - 100]:
        v.remove(p)

target = 10**12 - 1
v = set([(x, 0) for x in range(7)])
top = 0
idx = -1
part1 = None
tracker = defaultdict(list)
initial = None
divisor = None
amount = None
tgtidx = -1

while True:
    idx += 1
    rock = [[x+2, y+top+4] for x, y in next(rocks)]
    while True:
        dir = jetdir[next(jets)]
        if checkwalls(rock, dir) and checkblock(rock, v, dir, 0):
            tlx(rock, dir)
        if not checkblock(rock, v, 0, -1):
            break
        tly(rock, -1)
    v.update([(x, y) for x, y in rock])
    top = max([p[1] for p in rock] + [top])
    prune(v, top)

    if idx == 2021:
        print("p1: ", top)

    if idx == tgtidx:
        modulus = top - (initial + ((idx // divisor) - 1) * amount)
        part2 = initial + ((target // divisor) - 1) * amount + modulus
        print("p2: ", part2)
        break

    if divisor is not None:
        continue

    if idx != 0:
        tracker[idx] = [(top, top)]

    for i in [i for i in tracker if idx % i == 0]:
        tracker[i].append((top, top-tracker[i][-1][0]))
        if len(tracker[i]) > 3 and tracker[i][-1][1] == tracker[i][-2][1] == tracker[i][-3][1] == tracker[i][-4][1]:
            divisor = i
            initial = tracker[i][0][0]
            amount = tracker[i][-1][1]
            tgtidx = idx + (target % divisor)
            tracker = None
            break
        elif len(tracker[i]) > 3 and tracker[i][-1][1] != tracker[i][-2][1]:
            del tracker[i]
