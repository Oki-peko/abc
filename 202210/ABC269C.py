N = int(input())
ans = [0]

for i in range(60):
    if (N & (1<<i)):
        sz = len(ans)
        for j in range(sz):
            ans.append(ans[j]|(1<<i))

print(*ans,sep="\n")