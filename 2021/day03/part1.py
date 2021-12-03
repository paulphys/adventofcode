def power_consumption():
    with open ('input.txt', 'r') as f:
        binary = list(zip(*f.read().splitlines()))
    output = []
    for x in binary:
        output.append(sum(list(map(int,x))) > 500)
    epsilon = int("".join(str(int(b)) for b in output), base=2)
    gamma = int("".join(str(int(b)) for b in list(not r for r in output)), base=2)
    print(epsilon*gamma)

power_consumption()
