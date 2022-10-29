N,K = map(int,input().split())
a = list(map(int,input().split()))

sorted_a = sorted(a)

for i in range(N-K):
    if a[i] > a[i+K]:
        a[i+K],a[i] = a[i],a[i+K]

for i in reversed(range(N-K)):
    if a[i] > a[i+K]:
        a[i+K],a[i] = a[i],a[i+K]

print(sorted_a)
print(a)

if sorted_a == a:
    print("Yes")
else:
    print("No")