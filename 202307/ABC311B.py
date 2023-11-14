N, D = map(int, input().split())
S = [input() for _ in range(N)]

print(S)

ans = 0
max_tmp = 0

for day in range(D):
    flg = True
    for ok in range(N):
        if S[ok][day] == "x":
            max_tmp = 0
            flg = False
            break
    if flg:
        max_tmp += 1
        ans = max(ans, max_tmp)

print(ans)
