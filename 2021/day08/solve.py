from collections import Counter

def part1():
    display = [x[1].split() for x in (y.strip().split(" | ") for y in open("input.txt").readlines())]
    return len([digit for digits in display for digit in digits if len(digit) in [2,3,4,7]])

def part2():
    display = [x.split("|") for x in open("input.txt")]
    digits = {"abcefg": "0", "cf": "1",
              "acdeg": "2", "acdfg": "3",
              "bcdf": "4", "abdfg": "5",
              "abdefg": "6", "acf": "7",
              "abcdefg": "8", "abcdfg": "9"}
    numbers = []
    for line in display:
        counts = Counter(line[0].replace(" ",""))
        transform = {x[0]: {4:"e",6:"b",9:"f"}[x[1]] for x in counts.items() if x[1] in (4,6,9)}
        for x in line[0].split():
            if len(x) == 2:
                transform.update({y: "c" for y in x if y not in transform})
        transform.update({x[0]: "a" for x in counts.items() if x[1] == 8 and x[0] not in transform})
        for x in line[0].split():
            if len(x) == 4:
                transform.update({y: "d" for y in x if y not in transform})
        transform.update({x[0]: "g" for x in counts.items() if x[1] == 7 and x[0] not in transform})
        numbers.append(int("".join([digits["".join(sorted(x))] for x in line[1].translate(str.maketrans(transform)).split()])))
    return sum(numbers)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
