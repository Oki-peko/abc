N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

order = -1
tmp = -1

ans = [0]*N

for i in range(N):
    if tmp != A[i]:
        order += 1
    ans[order] += 1
    tmp = A[i]

print(*ans,sep="\n")