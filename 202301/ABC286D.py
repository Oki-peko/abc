N,X = map(int,input().split()) 
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in reversed(range(N)):
    for j in range(B[i]):
        