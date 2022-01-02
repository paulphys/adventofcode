input = [int(x) for x in open("input.txt").read().splitlines()]

def count(input):
    increments = 0
    previous = input[0]
    for i in input:
        if i > previous:
            increments += 1
        previous = i
    return increments

summed_windows = [sum(x) for x in zip(input, input[1:], input[2:])]

print(f"Part 1: {count(input)}")
print(f"Part 2: {count(summed_windows)}")
