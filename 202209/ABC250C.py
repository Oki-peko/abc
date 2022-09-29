N,Q = map(int,input().split())
val = [i for i in range(N+1)]
pos = [i for i in range(N+1)]

for i in range(Q):
    x = int(input())
    p0 = pos[x]
    p1 = p0
    if p0 != N:
        p1+=1
    else:
        p1-=1
    v0 = val[p0]
    v1 = val[p1]
    val[p0],val[p1] = val[p1],val[p0]
    pos[v0],pos[v1] = pos[v1],pos[v0]

print(*val[1:])