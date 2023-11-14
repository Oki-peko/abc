N,M = map(int,input().split())
F = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
  for j in range(N):
    if F[i][0] <= F[j][0]:
        if set(F[j][2:]).issubset(set(F[i][2:])):
          if F[i][0] < F[j][0]:
            print("Yes")
            exit()
          if len(F[i]) > len(F[j]):
            print("Yes")
            exit()

print("No")