def squidbingo():
    with open("input.txt") as f:
        numbers = [int(x) for x in f.readline().split(",")]
        boards = []
        for line in f:
            board = [list(map(int, f.readline().split())) for x in range(5)]
            boards.append(board)
    for number in numbers:
        boards = [[[num if num != number else False for num in row] for row in board] for board in boards]
        for x, board in enumerate(boards):
            if any(all(num is False for num in row) for row in board) or \
                    any(all(num is False for num in row) for row in zip(*board)):
                yield number * sum(map(sum, board))
                del boards[x]

game = list(squidbingo())

print(f"Part 1: {game[0]}")
print(f"Part 2: {game[-1]}")
