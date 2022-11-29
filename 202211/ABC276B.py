N,M = map(int,input().split())
ans = [[0] for _ in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    ans[A-1].append(B)
    ans[B-1].append(A)
    ans[A-1][0] += 1
    ans[B-1][0] += 1

for i in range(N):
    ans[i] = [ans[i][0]] + sorted(ans[i][1:])
    print(*ans[i])