from itertools import product
from math import prod
import re

input = open("input.txt").read().splitlines()
instructions = [(re.search('(on|off)', x).group(), list(map(int, (y.group() for y in re.finditer('-?\d+', x))))) for x in input]

def get_overlap(c1, c2):
    overlap = []
    for i in range(0,6,2):
        if c1[i+1] >= c2[i] and c1[i] <= c2[i+1]:
            overlap += [max(c1[i], c2[i]), min(c1[i+1], c2[i+1])]
        else:
            return None
    return overlap

def split_cuboid(cuboid, overlap):
    new_cuboids = []
    if cuboid[0] != overlap[0]:
        new_cuboids.append([cuboid[0], overlap[0]-1, *cuboid[2:]])
    if cuboid[1] != overlap[1]:
        new_cuboids.append([overlap[1]+1, cuboid[1], *cuboid[2:]])
    if cuboid[2] != overlap[2]:
        new_cuboids.append([*overlap[:2], cuboid[2], overlap[2]-1, *cuboid[4:]])
    if cuboid[3] != overlap[3]:
        new_cuboids.append([*overlap[:2], overlap[3]+1, cuboid[3], *cuboid[4:]])
    if cuboid[4] != overlap[4]:
        new_cuboids.append([*overlap[:4], cuboid[4], overlap[4]-1])
    if cuboid[5] != overlap[5]:
        new_cuboids.append([*overlap[:4], overlap[5]+1, cuboid[5]])
    return new_cuboids

cuboids_on = []
for action, cuboid in instructions:
    if len(cuboids_on) == 0:
        if action == 'on':
            cuboids_on.append(cuboid)
            continue
        else: continue
    else:
        to_remove = []
        if action == 'on': new_cuboids = [cuboid]
        else: new_cuboids = []
        for i, cuboid_on in enumerate(cuboids_on):
            overlap = get_overlap(cuboid_on, cuboid)
            if overlap is not None:
                to_remove.append(i)
                new_cuboids += split_cuboid(cuboid_on, overlap)
        for i in reversed(to_remove):
            del cuboids_on[i]
        cuboids_on += new_cuboids

answer1 = sum([prod([abs(x[i]-x[i+1])+1 for i in range(0,6,2)]) for x in cuboids_on if -50<=x[0]<=50])
answer2 = sum([prod([abs(x[i]-x[i+1])+1 for i in range(0,6,2)]) for x in cuboids_on])

print(answer1,answer2)
