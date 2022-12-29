N,M = map(int,input().split())
S = []
ans = 0
for i in range(N):
    S.append(input())

for i in range(N):
    for j in range(i+1,N):
        flg = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                flg = False
                break
        if flg == True:
            ans += 1

print(ans)