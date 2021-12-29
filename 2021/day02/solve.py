commands = open("input.txt").read().splitlines()

def part1():
    depth,horizontal = 0,0
    for x in range(len(commands)):
        direction = commands[x].split()[0]
        value = int(commands[x].split()[1])
        if direction == 'forward':
            horizontal += value
        if direction == 'down':
            depth += value
        if direction == 'up':
            depth -= value
    return depth * horizontal

def part2():
    depth,horizontal,aim = 0,0,0
    for x in range(len(commands)):
        direction = commands[x].split()[0]
        value = int(commands[x].split()[1])
        if direction == 'forward':
            horizontal += value
            depth += aim * value
        if direction == 'down':
            aim += value
        if direction == 'up':
            aim -= value
    return depth * horizontal

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
