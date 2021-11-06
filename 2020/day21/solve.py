input = open('input.txt', 'rt').read().splitlines()

allergens = {}
ingredients = []

for i in input:
    a,b = i.rstrip(")").split("(contains ")
    ingredient = a.split()
    ingredients.append(ingredient)
    for a in b.split(", "):
        if a not in allergens: allergens[a] = set(ingredient)
        else: allergens[a] &= set(ingredient)
    all_allergens = set(i for a in allergens.values() for i in a)
    sum_ingredients = sum(i not in all_allergens for ingredient in ingredients for i in ingredient)
print(sum_ingredients)

def remove(a,allergens):
    lonely = set()
    for k in allergens:
        if len(allergens[k])> 1 and a in allergens[k]:
                allergens[k].remove(a)
                if len(allergens[k])==1:
                    lonely |= allergens[k]
    return lonely

r = next(list(v) for v in allergens.values() if len(v)==1)
while r:
    r += list(remove(r.pop(),allergens))
print(','.join(str(i.pop()) for a,i in sorted((k,v) for k,v in allergens.items())))



