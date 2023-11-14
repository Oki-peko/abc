N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(M)]

OK_list = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
  OK_list[i][i] = 1

for i in range(M):
  for j in range(N-1):
    OK_list[a[i][j]-1][a[i][j+1]-1] = 1
    OK_list[a[i][j+1]-1][a[i][j]-1] = 1

cnt = 0
for i in range(N):
  for j in range(N):
    if OK_list[i][j] == 0:
      cnt += 1

print(OK_list)
print(cnt // 2)