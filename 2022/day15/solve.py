import re

manhattan = lambda x: ((x[0], x[1]), abs(x[2]-x[0])+abs(x[3]-x[1]))

data = [[int(x) for x in re.findall(r'(-?\d+)',line)] for line in open("input.txt").read().splitlines()]
beacons = dict([((x[2],x[3]), 0) for x in data])
sensors = dict([manhattan(x) for x in data])

def interval_union(i):
    if not i: return []
    i = sorted(i, key=lambda x: x[0])
    result = [i.pop(0),]
    while i:
        if result[-1][1] >= i[0][0]:
            if i[0][1] >= result[-1][1]:
                result[-1][1] = i[0][1]
            i.pop(0)
        else:
            result.append(i.pop(0))
    return result

def find_holes(line_no, grid):
    intervals = []
    for sensor in grid.keys():
        remainder = grid[sensor]-abs(sensor[1]-line_no) 
        if remainder >= 0:
            intervals.append([sensor[0]-remainder, sensor[0]+remainder])  
    return intervals

line = 2*10**6
part1 = sum([x[1]-x[0]+1 for x in interval_union(find_holes(line, sensors))])

corrector = sum([1 for x in sensors.keys() if x[1] == line]+[1 for x in beacons if x[1] == line])
print("p1: ", part1 - corrector)

lines = 4*10**6
for ii in range(0,lines+1):
    tmp = interval_union(find_holes(ii, sensors))
    if len(tmp) == 2 and (-1 <= tmp[0][1] < lines):
        print((tmp[0][1]+1)*lines+ii)
        break
