f = open('input.txt')
l = [int(line) for line in f]
for a in range(len(l)):
    for b in range(a+1,len(l)):
        for c in range(b+1,len(l)):
            if l[a] + l[b] +l[c]== 2020:
                print(l[a]*l[b]*l[c])
