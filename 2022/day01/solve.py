calories = open("input.txt").read().split("\n\n")
most = sorted(sum(int(snack) for snack in line.splitlines()) for line in calories)
print(f"p1: {most[-1]}")
print(f"p2: {sum(most[-3:])}")
