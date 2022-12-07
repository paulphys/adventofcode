import os.path
from collections import defaultdict

lines,d = [line.strip() for line in open("input.txt").readlines()], defaultdict(int)

def part_one():
    c = "/"
    for line in lines:
        s = line.split(" ")
        if s[0] == "$":
            command = s[1]
            if command == "cd":
                if s[2] == "..":
                    c = os.path.dirname(c)
                else:
                    c = os.path.join(c, s[2])
        elif s[0].isnumeric():
            d[c] += int(s[0])
            temp = c

            while os.path.dirname(temp) != temp:
                temp = os.path.dirname(temp)
                d[temp] += int(s[0])

    t = sum (v for v in d.values() if v <= 10**5)
    return t

def part_two():
    space= 3*10**7 - (7*10**7 - d["/"])
    return min(size for size in d.values() if size >= space)

print(f"p1: {part_one()}")
print(f"p2: {part_two()}")
