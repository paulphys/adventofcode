grid = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      grid.append(line)

product = 1
for drow, dcol in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
  trees = 0
  row, col = 0, 0
  while row < len(grid):
    location = grid[row][col]
    if location == '#':
      trees += 1
    row += drow
    col = (col + dcol) % len(grid[0])
  product *= trees

print(product)
