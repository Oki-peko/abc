N = int(input())
A = list(map(int,input().split()))

gen = [0]*(N*2+1)
parent = [0]*(N*2+1)
last = 0

for i in range(N):
    last += 1
    parent[last] = A[i]
    last += 1
    parent[last] = A[i]

for i in range(1,len(parent)):
    gen[i] = gen[parent[i]-1]+1

print(*gen)