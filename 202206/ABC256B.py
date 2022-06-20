N = int(input())
hit = list(map(int,input().split()))
A = [0]*4
P = 0

for i in range(N):
  A[0] = 1
  for j in range(3,-1,-1):
    if A[j] == 1:
      A[j] = 0
      if hit[i] + j >= 4:
        P += 1
      else:
        A[hit[i] + j] = 1

print(P)