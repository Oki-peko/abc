N,M = map(int,input().split())
x = []

for i in range(M):
    x.append(list(map(int,input().split())))

pair = [[False for i in range(N)] for j in range(N)]

for i in range(M):
    for j in range(1,x[i][0]+1):
        for k in range(1,x[i][0]+1):
            pair[x[i][j]-1][x[i][k]-1] = True

for i in range(N):
    for j in range(N):
        if pair[i][j] == False:
            print("No")
            exit()

print("Yes")