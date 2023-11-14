N,M = map(int,input().split())
A = list(map(int,input().split()))+[10**11]
B = list(map(int,input().split()))+[10**11]
ansA = []
ansB = []

max = 0
tmpA = 0
tmpB = 0

for i in range(1,N+M+1):
  if A[tmpA] < B[tmpB]:
    ansA.append(i)
    tmpA += 1
  else:
    ansB.append(i)
    tmpB += 1

print(*ansA)
print(*ansB)