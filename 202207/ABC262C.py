N = int(input())
a = list(map(int,input().split()))
ans = 0
same = 0
dif = 0

pair_a = list(sorted(enumerate(a,1), key=lambda x: x[1]))

for i in range(N):
    if pair_a[i][0] == pair_a[i][1]:
        same += 1
    elif pair_a[i][0] == pair_a[pair_a[i][0]-1][1]:
        dif += 1

ans += same * (same - 1) // 2

for i in range(N):
  a[i] -= 1

for (i, j) in enumerate(a):
  if i < j and a[j] == i:
    ans += 1

print(ans)