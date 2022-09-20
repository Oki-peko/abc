N = int(input())
P = [0] + list(map(int,input().split()))

tmp = P[N-1]
ans = 0

for i in range(N):
  tmp = P[tmp-1]
  ans += 1
  
  if tmp == 0:
    print(ans)
