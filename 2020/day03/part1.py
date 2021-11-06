grid = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      grid.append(line)

trees = 0
row, col = 0, 0
drow, dcol = 1, 3

while row < len(grid):
  location = grid[row][col]
  if location == '#':
    trees += 1
  row += drow
  col = (col + dcol) % len(grid[0])

print(trees)
