import itertools
from functools import cache

start = open("input.txt").read().splitlines()
p1_pos, p2_pos = int(start[0][-1]), int(start[1][-1])
p1_score, p2_score, die, p1_turn = 0, 0, 0, True

def classic_dirac(p1_pos, p2_pos, p1_score, p2_score, die, p1_turn):
    while p1_score < 1000 and p2_score < 1000:
        die += 3
        mov_pos = 3 * die - 3
        if p1_turn:
            p1_pos = (p1_pos + mov_pos -1) % 10 + 1
            p1_score += p1_pos
        else:
            p2_pos = (p2_pos + mov_pos -1) % 10 + 1
            p2_score += p2_pos
        p1_turn = not p1_turn
    return (p1_score if p1_score < p2_score else p2_score) * die

@cache
def quantum_dirac(p1_pos, p1_score, p2_pos, p2_score, p1_turn):
    throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]
    if p1_score >= 21: return 1, 0
    if p2_score >= 21: return 0, 1
    pos = p1_pos if p1_turn else p2_pos
    new_positions = [(pos + throw - 1) % 10 + 1 for throw in throws]
    if p1_turn:
        subgames = (quantum_dirac(new_pos, p1_score + new_pos, p2_pos, p2_score, False) for new_pos in new_positions)
    else:
        subgames = (quantum_dirac(p1_pos, p1_score, new_pos, p2_score + new_pos, True) for new_pos in new_positions)
    return sum(p1 for p1, _ in subgames), sum(p2 for _, p2 in subgames)

print(f"Part 1: {classic_dirac(p1_pos,p2_pos,p1_score,p2_score,die,p1_turn)}")
print(f"Part 2: {max(quantum_dirac(p1_pos,0,p2_pos,0, True))}")
