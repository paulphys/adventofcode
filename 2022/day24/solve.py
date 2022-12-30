# slow af

from collections import defaultdict
from math import lcm
import networkx as nx

ls = open("input.txt").read().splitlines()
rows = len(ls) - 2
cols = len(ls[0]) - 2
inner = {j + i * 1j: ls[i + 1][j + 1] for i in range(rows) for j in range(cols)}
directions = {"<": -1, ">": 1, "^": -1j, "v": 1j}
blizzards = defaultdict(set)
steps = lcm(rows, cols)

for z in inner:
    if dz := directions.get(inner[z]):
        for t in range(steps):
            blizzards[t].add(z)
            z += dz
            z = (z.real % cols) + (z.imag % rows) * 1j

start = -1j
end = cols - 1 + rows * 1j
free = {k: (inner.keys() - v) | {start, end} for k, v in blizzards.items()}

G = nx.DiGraph()
for t1 in range(steps):
    G.add_edge((t1, start), "superstart")
    G.add_edge((t1, end), "superend")
    t2 = (t1 + 1) % steps
    G.add_edges_from(
        ((t1, z), (t2, w))
        for z in free[t1]
        for w in {z + dz for dz in (0, 1, -1, -1j, 1j)} & free[t2]
    )

time1 = nx.shortest_path_length(G, (0, start), "superend") - 1
print("p1: ", time1)

time2 = nx.shortest_path_length(G, (time1 % steps, end), "superstart") - 1
time3 = nx.shortest_path_length(G, ((time1 + time2) % steps, start), "superend") - 1
print("p2: ", time1 + time2 + time3)
