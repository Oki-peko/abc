N = int(input())
S = [list(map(int, (input()))) for S in range(N)]

print(S)

ans = 1001001001

for x in range(10):
    num = [0]*10
    for i in range(N):
        for j in range(10):
            if S[i][j] == x:
                num[j] += 1

    now = 0

    for i in range(10):
        t = i+10*(num[i]-1)
        now = max(now, t)

    ans = min(ans, now)

print(ans)
