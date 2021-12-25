import numpy as np
lines = open("input.txt").read().splitlines()
grid = np.array([list(line) for line in lines])

def step(herd: str, grid: np.ndarray) -> int:
	move = grid == herd
	gridShiftedBack = np.roll(grid, -1, 1 if herd == ">" else 0)
	move[gridShiftedBack != '.'] = False
	grid[move] = '.'
	toMoveShiftedForward = np.roll(move, 1, 1 if herd == ">" else 0)
	grid[toMoveShiftedForward] = herd
	return len(grid[move])

def locator():
	count = 1
	while step('>', grid) + step('v', grid) > 0:
		count += 1
	print(count)

locator()
