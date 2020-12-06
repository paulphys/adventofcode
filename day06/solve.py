form = open('input.txt').read().split('\n\n')

def part1(form):
  return len(set(form.replace('\n','')))

def part2(form):
  questions = set(form.replace('\n',''))
  answers = form.split()
  return sum(all(q in a for a in answers) for q in questions)

print(sum(part1(g) for i in form))
print(sum(part2(g) for i in form))
