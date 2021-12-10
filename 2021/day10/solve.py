from functools import reduce

chunks = open("input.txt").read().splitlines()

def chunklist(line, scoring):
    chars= {"(": ")", "[": "]", "{": "}", "<": ">"}
    count = []
    for x in line:
        if x in chars:
            count.append(chars[x])
        elif x != count.pop():
            return scoring(x, [])
    return scoring(None, count)

def syntax_score(x, _):
    scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return scoring[x] if x else 0

def end_score(_, count):
    scoring = {")": 1, "]": 2, "}": 3, ">": 4}
    return reduce(lambda x, y: x * 5 + scoring[y], reversed(count), 0)

scores = sorted(filter(bool, (chunklist(y, end_score) for y in chunks)))
print(f'Part 1: {sum(chunklist(y, syntax_score) for y in chunks)}')
print(f'Part 2: {scores[len(scores) // 2]}')

## credits to @RealFenlair on reddit for this elegant solution
