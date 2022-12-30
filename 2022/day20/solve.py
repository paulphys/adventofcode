from itertools import cycle

key = 811589153

def solve(task):
    rounds, mutliply = (1, 1) if task == 1 else (10, key)
    numbers = [int(n) * mutliply for n in open("input.txt").readlines()]
    mixed = [a for a in enumerate(numbers)]
    cyc = cycle(mixed.copy())
    zero_tuple = (numbers.index(0), 0)
    lm = len(mixed) - 1

    for _ in range(rounds * len(numbers)):
        curr = next(cyc)
        idx_old = mixed.index(curr)
        mixed.remove(curr)
        idx_new = (idx_old + curr[1] + lm) % lm
        mixed.insert(idx_new, curr)

    idx_zero_tuple = mixed.index(zero_tuple)
    return (sum([mixed[(idx_zero_tuple + i) % len(numbers)][1]for i in [1000, 2000, 3000]]))

print("p1: ",solve(task=1))
print("p2: ",solve(task=2))
