with open('input.txt', 'r') as f:
    input = f.read()

def count(input):
    increments = 0
    previous = input[0]
    for i in input:
        if i > previous:
            increments += 1
        previous = i
    return increments

measurements = [int(x) for x in input.splitlines()]
summed_windows = [sum(x) for x in zip(measurements, measurements[1:], measurements[2:])]

print(f"Part 1: {count(measurements)}")
print(f"Part 2: {count(summed_windows)}")
