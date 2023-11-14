import copy

N = int(input())
A = [list(input())  for _ in range(N)]
ans = copy.deepcopy(A)

print(ans)

for i in range(N):
    for j in range(N):
        if i==0 or j==0 or i==N-1 or j==N-1:
            if i==0 and j<N-1:
                ans[i][j+1]=A[i][j]
            if i<N-1 and j==N-1:
                ans[i+1][j]=A[i][j]
            if i==N-1 and j>0:
                ans[i][j-1]=A[i][j]
            if i>0 and j==0:
                ans[i-1][j]=A[i][j]

for i in range(N):
    print(''.join(ans[i]))