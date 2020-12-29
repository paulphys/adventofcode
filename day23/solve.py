def crabcups(cups, moves, pad):
    nex = [i + 1 for i in range(pad + 1)]
    for i, label in enumerate(cups[:-1]):
        nex[label] = cups[i + 1]
    head = cups[0]
    if pad > len(cups):
        nex[-1] = head
        nex[cups[-1]] = max(cups) + 1
    else:
        nex[cups[-1]] = head
    for i in range(moves):
        rem = nex[head]
        nex[head] = nex[nex[nex[rem]]]
        allrem = rem, nex[rem], nex[nex[rem]]

        dest = head - 1 if head > 1 else pad
        while dest in allrem:
            dest = pad if dest == 1 else dest - 1

        nex[nex[nex[rem]]] = nex[dest]
        nex[dest] = rem
        head = nex[head]
    cup = nex[1]
    while cup != 1:
        yield cup
        cup = nex[cup]

cups = list(map(int, '215694783'))
print(''.join(map(str, crabcups(cups, 100, len(cups)))))
p2 = crabcups(cups, 10**7, 10**6)
print(next(p2) * next(p2))
