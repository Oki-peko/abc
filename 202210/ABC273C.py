import numpy as np

N = int(input())
A = list(map(int,input().split()))

sorted_A_index = np.argsort(A)
order = -1
tmp = -1

K = [0]*N

for i in sorted_A_index:
    if tmp != A[i]:
        order += 1
    K[i] = order
    tmp = A[i]

K = [max(K)-x for x in K]

ans = [0]*N

for i in K:
    ans[i] += 1

print(*ans,sep="\n")