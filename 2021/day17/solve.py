def trickshot():
    minx, maxx, miny, maxy = sum([[int(y) for y in x.split('=')[1].split('..')] for x in open("input.txt").read().split(', ')], [])
    count, best = 0, 0
    for dx in range(1, maxx + 1):
        for dy in range(miny, -maxy + (maxy - miny)):
            x, y, h = 0, 0, 0
            vx, vy = dx, dy
            while vx > 0 or y > miny:
                x, y, h = x + vx, y + vy, max(h,y)
                vx, vy = max(0, vx - 1), vy - 1
                if minx <= x <= maxx and miny <= y <= maxy:
                    count += 1
                    best = max(best, h)
                    break
    return best, count

print(trickshot())
