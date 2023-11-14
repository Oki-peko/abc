import itertools

N,M = map(int,input().split())
nums = list(range(1,N+1))
ans = 0

C = []
a = []
for _ in range(M):
  C.append(int(input()))
  a.append(list(map(int,input().split())))

patterns = []
for i in range(1,N+1):
    patterns += list(itertools.combinations(a, i))

for p in patterns:
    compare = []
    for n in p:
        compare += n
    print(set(compare))
    if set(compare) == set(nums):
        ans += 1

print(ans)