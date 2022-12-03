bags = [bag.strip() for bag in open("input.txt").readlines()]
alphabet = list(map(chr,range(97,123))) + list(map(chr,range(65,91)))
priority = 0

for bag in bags:
    c1, c2 = bag[:len(bag)//2], bag[len(bag)//2:]
    items = list(set(c1)&set(c2))
    for item in items:
        priority += alphabet.index(item)+1

print(f"p1: {priority}")

priority = 0
groups = [bags[i:i+3] for i in range(0,len(bags),3)]

for group in groups:
    badge = set.intersection(*map(set,group)).pop()
    priority += alphabet.index(badge)+1

print(f"p2: {priority}")
    
