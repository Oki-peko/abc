N, Q = map(int, input().split())

val = list(range(N+1))

for i in range(Q):
    x = int(input())
    p0 = val[x]
    p1 = p0
    if p0 != N:
        p1 += 1
    else:
        p1 -= 1
    val[p0],val[p1] = val[p1],val[p0]

print(*val[1:])
