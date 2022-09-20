x = int(input())
res = [0]

for d in range(60):
    sd = 1 << d
    if (x & sd):
        sz = len(res)
        for i in range(sz):
            res.append(res[i]|sd)

res.sort()
print(res)