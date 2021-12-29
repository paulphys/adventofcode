def power_consumption():
    binary = list(zip(*open("input.txt").read().splitlines()))
    output = []
    for x in binary:
        output.append(sum(list(map(int,x))) > 500)
    epsilon = int("".join(str(int(b)) for b in output), base=2)
    gamma = int("".join(str(int(b)) for b in list(not r for r in output)), base=2)
    return epsilon*gamma

print(f"Part 1: {power_consumption()}")
