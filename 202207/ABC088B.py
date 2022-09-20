N = int(input())
a = list(map(int,input().split()))
ans = 0

sorted_a = sorted(a,reverse=True)

for i in range(N):
    if i % 2 == 0:
        ans += sorted_a[i]
    else:
        ans -= sorted_a[i]

print(ans)