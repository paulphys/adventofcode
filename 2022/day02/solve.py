guide = [game.strip() for game in open("input.txt").readlines()]
p1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
p2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
total_p1 = sum(p1[game] for game in guide)
total_p2 = sum(p2[game] for game in guide)
print(f"p1: {total_p1}")
print(f"p2: {total_p2}")
