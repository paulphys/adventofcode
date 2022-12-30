from functools import reduce

req = open("input.txt").read().splitlines()

def toDec(num):
    return reduce(
        lambda r, v: (
            r[0] + ("=-012".index(v) - 2)* r[1],
            r[1] * 5,),
        num[::-1],
        (0, 1),
    )[0]

def toSNAFU(num):
    res = []
    while num > 0:
        res.append("012=-"[num % 5])
        num = (2 + num) // 5
    return ''.join(res[::-1])

print(toSNAFU(sum(toDec(l) for l in req)))
