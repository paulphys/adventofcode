def fish_population(days):
    fish = [[int(x) for x in open("input.txt").read().split(",")].count(x) for x in range(0, 9)]
    for x in range(0, days):
        fish = fish[1:] + fish[:1]
        fish[6] += fish[8]
    return (sum(fish))

print(f"Part 1: {fish_population(80)}")
print(f"Part 2: {fish_population(256)}")
