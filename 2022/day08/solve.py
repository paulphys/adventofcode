trees = open("input.txt").read().strip().splitlines()
visible, scenic = set(), 0

for x in range(len(trees)):
    for y in range(len(trees)):
        score = 1
        pos = trees[x][y]
        left = trees[x][:y][::-1]
        right = trees[x][y+1:len(trees)]
        up = [trees[nx][y] for nx in reversed(range(x))]
        down = [trees[nx][y] for nx in range(x+1,len(trees))]
        
        for direction in left, right, up, down:
            for n, neighbour in enumerate(direction):
                if pos <= neighbour:
                    score *= n+1; break
            else:
                score *= len(direction) if direction else 1
                visible.add((x,y))
        scenic = max(scenic, score)
    
print(f"p1: {len(visible)}")
print(f"p2: {scenic}")
