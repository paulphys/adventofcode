instructions = open("input.txt").read().strip().splitlines()

visisted = set()
rope = [(0, 0) for i in range(2)] # 10 for part 2

def move(rope, direction, steps):
    for i in range(steps):
        head_x, head_y = rope[0]
        if direction == 'R':
            head_x += 1
        elif direction == 'L':
            head_x -= 1
        elif direction == 'U':
            head_y += 1
        elif direction == 'D':
            head_y -= 1

        rope[0] = (head_x, head_y)

        for i in range(1, len(rope)):
            prev_x, prev_y = rope[i-1]
            curr_x, curr_y = rope[i]

            if abs(prev_x - curr_x) > 1 or abs(prev_y - curr_y) > 1:
                if prev_x > curr_x:
                    curr_x += 1
                elif prev_x < curr_x:
                    curr_x -= 1

                if prev_y > curr_y:
                    curr_y += 1
                elif prev_y < curr_y:
                    curr_y -= 1

            rope[i] = (curr_x, curr_y)
        visisted.add((curr_x, curr_y))

for x in instructions:
    direction, steps = x.split(' ')
    move(rope, direction, int(steps))

print(len(visisted))
