N = int(input())
A = [list(map(int,input())) for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

ans = 0

for i in range(N):
    for j in range(N):
        for d in range(8):
            now = ""
            x,y = i,j
            for k in range(N):
                now += str(A[x][y])
                x += dx[d]
                y += dy[d]
                x %= N
                y %= N
            if ans < int(now):
                ans = int(now)

print(ans)