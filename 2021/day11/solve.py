energy = [list(map(int, row)) for row in open("input.txt").read().splitlines()]

def step(energy):
    flashes, stack = 0, []
    for x in range(10):
        for y in range(10):
            energy[x][y] += 1
            if energy[x][y] > 9:
                flashes += 1
                energy[x][y] = 0
                stack.append((x,y))
    while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and energy[nx][ny] > 0:
                energy[nx][ny] += 1
                if energy[nx][ny] > 9:
                    flashes += 1
                    energy[nx][ny] = 0
                    stack.append((nx, ny))
    return flashes

def part1(energy):
    return sum(step(energy) for x in range(100))

def part2(energy):
    steps = 0
    while sum(map(sum, energy)) > 0:
        step(energy)
        steps += 1
    return steps

print(f"Part 1: {part1([row[:] for row in energy])}")
print(f"Part 2: {part2([row[:] for row in energy])}")
