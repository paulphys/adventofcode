import heapq as hq

rooms = {"A": 2, "B": 4, "C": 6, "D": 8}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
goal1 = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"))
goal2 = (
    ("A", "A", "A", "A"),
    ("B", "B", "B", "B"),
    ("C", "C", "C", "C"),
    ("D", "D", "D", "D")
)

def dijkstra(start, goal):
    q = [ (0, 0, (start, (None, None, None, None, None, None, None, None, None, None, None)))]
    hq.heapify(q)
    seen = set()
    while len(q):
        cost, _, (rooms, hallway) = hq.heappop(q)
        if rooms == goal:
            return cost
        if (rooms, hallway) in seen:
            continue
        seen.add((rooms, hallway))
        for i, room in enumerate(rooms):
            if room == goal[i]:
                continue
            try:
                j, c = next((j, c) for j, c in enumerate(room) if c)
            except StopIteration:
                continue
            for p in [0, 1, 3, 5, 7, 9, 10]:
                if all(
                    z is None
                        for z in hallway[min(2*i + 2, p):max(2*i + 2, p) + 1]
                ):
                    _cost = cost + costs[c]*(j + abs(2*i + 2 - p) + 1)
                    _rooms = tuple(
                        tuple(
                            None if (k == i and l == j) else c
                                for l, c in enumerate(room)
                        )
                            for k, room in enumerate(rooms)
                    )
                    _hallway = tuple(
                        c if k == p else h
                            for k, h in enumerate(hallway)
                    )

                    hq.heappush(
                        q, (_cost, id(_rooms), (_rooms, _hallway))
                    )

        for p in [0, 1, 3, 5, 7, 9, 10]:
            c = hallway[p]
            if c is None:
                continue

            path = hallway[rooms[c]:p] if p > rooms[c] else hallway[p + 1:rooms[c] + 1]
            if all(
                z is None for z in path
            ):
                i = ord(c) - ord('A')
                room = rooms[i]

                if all(
                    z in {None, c} for z in room
                ):
                    j = 0
                    while j < len(room) and room[j] is None:
                        j = j + 1
                    j = j - 1

                    if room[j] is not None:
                        continue

                    _cost = cost + costs[c]*(j + abs(rooms[c] - p) + 1)
                    _rooms = tuple(
                        tuple(
                            c if (k == i and l == j) else h
                                for l, h in enumerate(room)
                        )
                            for k, room in enumerate(rooms)
                    )
                    _hallway = tuple(
                        None if k == p else h
                            for k, h in enumerate(hallway)
                    )

                    hq.heappush(
                        q, (_cost, id(_rooms), (_rooms, _hallway))
                    )

rooms = (
    ("D", "B"),
    ("C", "A"),
    ("D", "A"),
    ("B", "C")
)

print(dijkstra(rooms, goal1))

rooms = (
    ("D", "D", "D", "B"),
    ("D", "C", "B", "A"),
    ("C", "B", "A", "B"),
    ("C", "A", "C", "A")
)

print(dijkstra(rooms, goal2))
