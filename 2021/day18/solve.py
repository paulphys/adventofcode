import functools

parsed = []
for line in open("input.txt").read().splitlines():
    parsed_line = []
    depth = 0
    for y in range(len(line)):
        if line[y] == '[':
            depth += 1
        elif line[y] ==  ']':
            depth -= 1
        elif line[y] == ',':
            pass
        else:
            parsed_line.append([int(line[y]),depth])
    parsed.append(parsed_line)

def addition(sn1, sn2):
    sum_sn = [[entry[0],entry[1]+1] for entry in sn1 + sn2]
    updated = True
    while updated:
        updated = False
        for i in range(len(sum_sn)):
            depth = sum_sn[i][1]
            if depth >= 5 and depth==sum_sn[i+1][1]:
                if i > 0:
                    sum_sn[i-1][0] += sum_sn[i][0]
                if i < len(sum_sn)-2:
                    sum_sn[i+2][0] += sum_sn[i+1][0]
                del sum_sn[i:i+2]
                sum_sn.insert(i,[0,depth-1])
                updated = True
                break
        if not updated:
            for i in range(len(sum_sn)):
                if sum_sn[i][0] > 9:
                    [val, depth] = sum_sn[i]
                    half_rounded_down = val//2
                    half_rounded_up = val - val//2
                    del sum_sn[i]
                    sum_sn.insert(i,[half_rounded_up, depth+1])
                    sum_sn.insert(i,[half_rounded_down, depth+1])
                    updated = True
                    break
    return sum_sn

def magnitude(sn):
    while len(sn) > 1:
        for i in range(len(sn)):
            if i < len(sn) - 1 and sn[i][1] == sn[i+1][1]:
                depth = sn[i][1]
                val = sn[i][0] * 3 + sn[i+1][0] * 2
                del sn[i:i+2]
                sn.insert(i,[val,depth-1])
                break
    return sn[0][0]

def snailmath():
    total = 0
    for x in range(len(parsed)-1):
        for y in range(x+1, len(parsed)):
            total = max(total, magnitude(addition(parsed[x], parsed[y])))
            total = max(total, magnitude(addition(parsed[y], parsed[x])))
    return magnitude(functools.reduce(addition,parsed)), total

print(snailmath())
