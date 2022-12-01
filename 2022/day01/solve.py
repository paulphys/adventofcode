calories = open("input.txt").read().split("\n\n")
data = sorted(sum(int(snack) for snack in line.splitlines()) for line in calories)
print(f"p1: {data[-1]}")
print(f"p2: {sum(data[-3:])}")
