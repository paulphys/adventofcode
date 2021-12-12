caves = [line.split("-") for line in open("input.txt").read().splitlines()]
caves += [pair[::-1] for pair in caves]

def part1():
    start = [['start']]
    end = []
    while len(start) > 0:
        path = start.pop(0)
        for current, target in caves:
            if current != path[-1]: continue
            if target.upper() != target and target in path:continue
            pathway = [path + [target]]
            if target == 'end':end += pathway
            else: start += pathway
    return len(end)

def part2():
    start = [[['start'],'']]
    end = []
    while len(start) > 0:
        path, twice = start.pop(0)
        for current, target in caves:
            if current != path[-1]:continue
            if target == 'start' or (target.upper() != target and target in path and twice != ""):continue
            pathway = [[path + [target], [twice,target][target.upper() != target and target in path]]]
            if target == 'end':end += pathway
            else: start += pathway
    return len(end)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
