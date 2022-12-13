game = open("input.txt").read().splitlines()
ops = [(game[x][23:]) for x in range(2, len(game), 7)]
test = [int(game[x][21:]) for x in range(3, len(game), 7)]
conds = [[int(game[x][29:]), int(game[x+1][30:])] for x in range(4, len(game), 7)]

modulo = 1
for x in test:
    modulo *= x

def solver(part):
    inspects = [0] * len(test)
    items = [[[int(x) for x in (game[y][18:]).split(", ")] for y in range(1, len(game), 7)]][0]
    for a in range(0, (20 if part == 1 else 10**3 if part == 2 else 0)):
        for b in range(0, len(inspects)):
            for c in range(0, len(items[b])):
                current = items[b][c]
                if ops[b] == "* old":
                    current *= current
                elif ops[b][:2] == "* ":
                    current *= int(ops[b][2:])
                elif ops[b][:2] == "+ ":
                    current += int(ops[b][2:])
                current = current // 3 if part == 1 else current % modulo
                if current % test[b] == 0:
                    items[conds[b][0]].append(current)
                else:
                    items[conds[b][1]].append(current)
                inspects[b] += 1
            items[b] = []
    return sorted(inspects)[-1]*sorted(inspects)[-2]

print("p1: ", solver(1))
print("p2: ", solver(2))
