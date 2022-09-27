N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

passed = [False] * N

C = []
for i in range(N):
    if passed[i] == False:
        C.append(10000*(100-A[i])+i)
C.sort()
for i in range(X):
    passed[C[i]%10000] = True

C = []
for i in range(N):
    if passed[i] == False:
        C.append(10000*(100-B[i])+i)
C.sort()
for i in range(Y):
    passed[C[i]%10000] = True

C = []
for i in range(N):
    if passed[i] == False:
        C.append(10000*(200-(A[i]+B[i]))+i)
C.sort()
for i in range(Z):
    passed[C[i]%10000] = True

for i in range(N):
    if passed[i]:
        print(i+1)