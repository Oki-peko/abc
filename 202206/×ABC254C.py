# https://atcoder.jp/contests/abc254/tasks/abc254_c
N,K = map(int,input().split())
A = list(map(int, input().split()))
 
for i in range(N):
  if i >= K:
    for j in range(i//K):
      if A[i-K*j] <= A[i-K*(j+1)]:
       A[i-K*j], A[i-K*(j+1)] = A[i-K*(j+1)], A[i-K*j]
      else:
        break
 
for i in range(N-1):
  if A[i] > A[i+1]:
    print("No")
    exit()
 
print("Yes")