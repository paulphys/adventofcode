sensor = open("input.txt").read().splitlines()
diff = [-1,0,1]
key = None
trench = set()
y = 0
for line in sensor:
    if not key:
        key = line
    elif len(line) > 0:
        for x in range(len(line)):
            if line[x] == '#':
                trench.add((x,y))
        y += 1

neighbours = set()
for point in trench:
    x,y = point
    for dx in diff:
        for dy in diff:
            neighbours.add((x+dx,y+dy))

def step(trench, neighbours, itr=0):
    itrKey = {'#':'1', '.':'0'}
    pointToSave = '#'
    if key[0] == '#' and key[-1] == '.':
        if itr > 0 and (itr%2) == 0:
            itrKey = {'#':'0', '.':'1'}
        else:
            pointToSave = '.'
    newTrench = set()
    newNeighbours = set()
    for point in neighbours:
        number = ''
        x,y = point
        for dy in diff:
            for dx in diff:
                if (x+dx, y+dy) in trench:
                    number += itrKey['#']
                else:
                    number += itrKey['.']
        if key[int(number,2)] == pointToSave:
            newTrench.add(point)
            for dy in diff:
                for dx in diff:
                    newNeighbours.add((x+dx,y+dy))
    return newTrench, newNeighbours

def mapping(trench):
    minY,minX = len(trench), len(trench)
    maxY,maxX = 0, 0
    for point in trench:
        x,y = point
        if y < minY: minY = y
        if y > maxY: maxY = y
        if x < minX: minX = x
        if x > maxX: maxX = x
    for y in range(minY,maxY+1):
        for x in range(minX,maxX+1):
            if (x,y) in trench:
                print('#',end='')
            else:
                print('.',end='')
        print('')
    print('')

for x in range(50):
    trench, neighbours = step(trench, neighbours, itr = x+1)
    if (x+1) == 2:
        print("Part 1: {}".format(len(trench)))
print("Part 2: {}".format(len(trench)))
