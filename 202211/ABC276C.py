N = int(input())
P = list(map(int,input().split()))
ans = P.copy()

last = P[N-1]
for i in reversed(range(N)):
    if last > P[i]:
        point = i
        break

ans[point] = P[point+1]
P[point:] = reversed(sorted(P[point:]))
ans[point+1:]=P[point+1:]

print(*ans)