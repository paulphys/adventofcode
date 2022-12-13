from collections import deque

def solver(*start):
    grid = open("input.txt").read().splitlines()
    Q = deque((i, j, 0, 'a') for i in range(len(grid)) 
        for j in range(len(grid[i])) 
        if grid[i][j] in start)

    visited = set((i, j) for i, j, _, _ in Q)

    def push(i, j, d, a):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]): return
        if (i, j) in visited: return

        b = grid[i][j].replace('E', 'z')
        if ord(b) > ord(a) + 1: return
        visited.add((i, j))
        Q.append((i, j, d + 1, b))

    while len(Q):
        i, j, d, a = Q.popleft()
        if grid[i][j] == 'E':
            return d

        push(i + 1, j, d, a)
        push(i - 1, j, d, a)
        push(i, j + 1, d, a)
        push(i, j - 1, d, a)

print(f"p1: {solver('S')}")
print(f"p2: {solver('S', 'a')}")
