N = int(input())
S = [list(map(int, input())) for i in range(N)]

ans = 1001001001

for x in range(10):
    cnt = [0]*10
    for i in range(N):
        for j in range(10):
            if x == S[i][j]:
                cnt[j] += 1

    now = 0

    for i in range(10):
        sec = (cnt[i]-1)*10 + i

        now = max(now, sec)

    ans = min(ans, now)

print(ans)
