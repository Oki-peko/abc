N,W = map(int,input().split())
A = list(map(int,input().split()))
ptn = []
for i in range(N):
    sum = A[i]
    if sum <= W:
        ptn.append(sum)
    for j in range(i+1,N):
        sum = A[i]+A[j]
        if sum <= W:
            ptn.append(sum)
        for k in range(j+1,N):
            sum = A[i]+A[j]+A[k]
            if sum <= W:
                ptn.append(sum)

print(len(set(ptn)))