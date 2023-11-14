N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))

ans = []
add = 0
tmp = 0

for i in range(N):
  add = A[i]
  if P-1 <= i <= Q-1:
    add = A[R-1+tmp]
    tmp += 1
  if i == Q-1:
    tmp = 0
  if R-1 <= i <= S-1:
    add = A[P-1+tmp]
    tmp += 1
  if i == S-1:
    tmp = 0
  ans.append(add)

print(ans)