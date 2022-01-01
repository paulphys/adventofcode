import numpy as np

pos = np.loadtxt("input.txt",delimiter=',',dtype=int)

def part1():
    return np.abs(pos-int(np.median(pos))).sum()

def part2():
    return int(((np.abs(pos-(round(np.mean(pos))-1))/2)*(np.abs(pos-(round(np.mean(pos))-1))+1)).sum())

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
