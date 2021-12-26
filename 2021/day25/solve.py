import numpy as np
grid = np.array([list(line) for line in open("input.txt").read().splitlines()])

def step(herd, grid):
	move = grid == herd
	ShiftedBack = np.roll(grid, -1, 1 if herd == ">" else 0)
	move[ShiftedBack != '.'] = False
	grid[move] = '.'
	toMove = np.roll(move, 1, 1 if herd == ">" else 0)
	grid[toMove] = herd
	return len(grid[move])

def locator():
    count = 1
    while step('>', grid) + step('v', grid) > 0:
        count += 1
    return count

print(f"Part 1: {locator()}")
