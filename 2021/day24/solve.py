from z3 import *

input = open('input.txt).read().splitlines()
lst = [[int(y.split()[-1]) for y in [input[x+4],input[x+5],input[x+15]]] for x in range(0,len(input),18)]

def ALU(max):
    z,v,s = 0,0,Optimize()
    for (i,[p,q,r]) in enumerate(lst):
        w = Int(f'w{i}')
        v = v * 10 + w
        s.add(And(w >= 1, w <= 9))
        z = If(z % 26 + q == w, z / p, z / p * 26 + w + r)
    s.add(z == 0)
    (s.maximize if max else s.minimize)(v)
    assert s.check() == sat
    return s.model().eval(v)

print(ALU(True))
print(ALU(False))
