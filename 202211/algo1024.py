N,M = map(int,input().split())
ans = 0

for x in range(1,N+1):
    for y in range(1,N+1):
        zs = M-(x+y)
        if zs >= N:
            zs = N
        if zs >= 0:
            ans += zs

print(ans)