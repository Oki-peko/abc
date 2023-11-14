N,A,B = map(int,input().split())
S = list(input())
SS = S*2
ans = 10**15

for i in range(N-1):
  price = i*A
  for j in range(N//2):
    if SS[j+i] != SS[N-1-j+i]:
      price += B
  
  ans = min(ans,price)

print(ans)