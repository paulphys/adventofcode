import numpy as np
import heapq

cavern = np.genfromtxt("input.txt", dtype=int, delimiter=1)
height, width = cavern.shape

def neighbors(x, y, scale):
    return [(a, b) for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= a < width*scale and 0 <= b < height*scale]

def cost(x, y):
    return 1+ (cavern[y % height, x % width] + x // width + y // height -1) % 9

def dijkstra(scale):
    distances = {(0,0):0}
    dj =[(0, (0,0))]
    while len(dj) > 0:
        total, (x,y) = heapq.heappop(dj)
        if total <= distances[(x, y)]:
            for n in neighbors(x, y, scale):
                distance = total + cost(*n)
                if distance < distances.get(n, 1e308):
                    distances[n] = distance
                    heapq.heappush(dj, (distance, n))
    return distances[(width*scale-1, height*scale-1)]

print("Part 1:", dijkstra(1))
print("Part 2:", dijkstra(5))
