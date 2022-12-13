from functools import cmp_to_key
import math 

groups = open("input.txt").read().split("\n\n")
pairs = []

for index, pair in enumerate(groups):
    lines = pair.split('\n');
    pairs.append((index, eval(lines[0]), eval(lines[1])))

def validator(p1, p2):
    for a, b in zip(p1, p2):

        if isinstance(a, list) and isinstance(b, list):
            result = validator(a, b)
            if result == True or result == False:
                return result

        elif isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
            else:
                pass 

        elif isinstance(a, int) and isinstance(b, list):
            result = validator([a], b)
            if result == True or result == False:
                return result
        elif isinstance(b, int) and isinstance(a, list):
            result = validator(a, [b])
            if result == True or result == False:
                return result

    if len(p1) > len(p2):
        return False
    elif len(p2) > len(p1):
        return True
    
valid_indexes = [index + 1 for index, p1, p2 in pairs if validator(p1, p2) == True]

print("p1: ",sum(valid_indexes))

cmp = cmp_to_key(lambda a, b: -1 if validator(a, b) else 1)

sorted_pairs = [[[2]], [[6]]]
for _, p1, p2 in pairs:
    sorted_pairs.append(p1)
    sorted_pairs.append(p2)

sorted_pairs.sort(key=cmp)
indexes = [index + 1 for index, packet in enumerate(sorted_pairs) if packet in [[[2]], [[6]]]]

print("p2: ",math.prod(indexes))
