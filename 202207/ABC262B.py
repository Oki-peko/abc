N ,M = map(int,input().split())
UV = []
ans = 0

for i in range(M):
    UV.append(list(input().split()))

for i in range(M):
    tmp = []
    for j in range(M):
        if UV[i][0] == UV[j][0]:
            if UV[j][1] in tmp:
                ans += 1
            tmp.append(UV[j][1])
        if UV[i][1] == UV[j][1]:
            if UV[j][0] in tmp:
                ans += 1
            tmp.append(UV[j][0])

print(ans)