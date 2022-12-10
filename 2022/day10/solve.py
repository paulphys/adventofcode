ops = open('input.txt').read().strip().replace('addx', 'noop\n').splitlines()
x, strength, crt = 1, 0, []

for cycle, op in enumerate(ops):
  if cycle in range(19,221,40):
      strength += (cycle+1) * x

  if cycle%40 == 0:
      crt.append('\n')
  
  crt.append('█' if abs((cycle%40)-x) < 2 else ' ')

  if op != 'noop':
      x += int(op)

print(f"p1: {strength}")
print(f"{''.join(crt)}")




