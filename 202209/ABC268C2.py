import itertools

n = int(input())
a = []
for i in range(60):
    if n & (1 << i):
        a.append(i)

k = len(a)
res = []
t = list(itertools.combinations_with_replacement(range(2), k))

for i in t:
    for j in range(len(i)):
        tmp = []
        for bit in range(60):
            if n & (1 << bit):
                tmp.append(i[j])
            else:
                tmp.append(0)
        res.append(tmp)

print(res)
