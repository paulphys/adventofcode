data = open("input.txt").readlines()

directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1),
              'NE': (-1, 1), 'SE': (1, 1), 'NW': (-1, -1), 'SW': (1, -1)}

heading = {'N': ('NW', 'N', 'NE'),
           'S': ('SW', 'S', 'SE'),
           'E': ('SE', 'E', 'NE'),
           'W': ('SW', 'W', 'NW'), }


def propose_move(elf, consider):
    y, x = elf
    possible = {direction: (y+yd, x+xd)
                for direction, (yd, xd)
                in directions.items()
                if (y+yd, x+xd) not in elves
                }
    if len(possible) == 8:
        return elf
    else:
        for to in consider:
            trio = heading[to]
            if len(set(trio).intersection(possible)) == 3:
                return possible[to]
        else:  
            return elf


def validate_moves(elves_consider):
    pos_count = {}
    for v in elves_consider.values():
        pos_count[v] = pos_count.get(v, 0) + 1
    return {k: (v if pos_count[v] == 1 else k) for (k, v) in elves_consider.items()}


def bounding_box(elves):
    yvals = [y for y, x in elves]
    xvals = [x for y, x in elves]
    y_min, y_max = min(yvals), max(yvals)
    x_min, x_max = min(xvals), max(xvals)
    area = (y_max - y_min + 1) * (x_max - x_min + 1)
    n_elves = len(elves)
    return area, n_elves, area - n_elves, (y_min, y_max), (x_min, x_max)


def starting_state():
    elves = set()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == '#':
                elves.add((y, x))
    consider = ['N', 'S', 'W', 'E']
    return elves, consider


def single_round(elves, consider):
    elves_consider = {elf: propose_move(elf, consider) for elf in elves}
    elves_next = validate_moves(elves_consider)
    elves = set(elves_next.values())
    consider = consider[1:] + [consider[0]]
    return elves, consider


elves, consider = starting_state()
for x in range(10):
    elves, consider = single_round(elves, consider)
print("p1: ", bounding_box(elves)[2])


elves, consider = starting_state()
for x in range(1000):  # this is so stupid but works
    elves_next, consider = single_round(elves, consider)
    if len(elves_next.intersection(elves)) == len(elves):
        print("p2: ", x+1)
        break
    else:
        elves = elves_next
