manual = open("input.txt").read().splitlines()
dots = [tuple(map(int,dot.split(','))) for dot in manual if ',' in dot]
instructions = [('y' in dot,int(dot[13:])) for dot in manual[len(dots)+1:]]
m = lambda n,Y: min([v+1 for y,v in n if Y^y] or [1e4])

def action(dots,instructions):
    b = lambda n,action: abs((n//action)%2*(action-2)-n%action)
    return set((b(x,m(instructions,1)),b(y,m(instructions,0))) for x,y in dots)

visible=action(dots,instructions)

print("Part 1: {:d}".format(len(action(dots,instructions[:1]))))
print("Part 2: \n{:s}".format('\n'.join(''.join(" #"[(x,y) in visible] for x in range(m(instructions,1))) for y in range(m(instructions,0)))))
