jobs = [job.strip() for job in open("input.txt").readlines()]
p1,p2 = 0,0

for pair in jobs:
    p = pair.split(",")
    j1, j2 = [int(x) for x in p[0].split("-")], [int(x) for x in p[1].split("-")]
    if (int(j1[0]) <= int(j2[0]) and int(j1[1]) >= int(j2[1])) or (int(j2[0]) <= int(j1[0]) and int(j2[1]) >= int(j1[1])):
        p1 += 1
    if not (j1[1] < j2[0] or j2[1] < j1[0]):
        p2 += 1

print(f"p1: {p1}")
print(f"p2: {p2}")

