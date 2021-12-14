from collections import Counter, defaultdict

def polymerization():
	rules = open("input.txt").read().splitlines()
	template = [x for x in rules[0]]
	pairs = dict(rule.split(" -> ") for rule in rules[2:])
	for x in range(10):
		insertions = []
		for y in range(len(template)-1):
			insertions.append(template[y])
			if template[y]+template[y+1] in pairs:
				insertions.append(pairs[template[y]+template[y+1]])
		insertions.append(template[-1])
		template = insertions
	poly = Counter(template).most_common()
	print(f"Part 1: {poly[0][1] - poly[-1][1]}")

	pair_count, occurences = defaultdict(int), defaultdict(int)
	template = rules[0]
	for x in template:
		occurences[x] += 1
	for pair in ("".join(pair) for pair in zip(template[:-1], template[1:])):
		pair_count[pair] += 1
	for y in range(40):
		for pair, count in pair_count.copy().items():
			new_char = pairs[pair]
			occurences[new_char] += count
			pair_count[pair] -= count
			pair_count[pair[0] + new_char] += count
			pair_count[new_char + pair[1]] += count
	print(f"Part 2: {max(occurences.values()) - min(occurences.values())}")

polymerization()
