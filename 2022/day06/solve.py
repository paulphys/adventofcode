stream = open("input.txt").read()

def decoder(m):
    for x in range(len(stream)):
        if len(set(stream[x:x+m])) == m:
            return x + m

print(f"p1: {decoder(4)}")
print(f"p2: {decoder(14)}")
