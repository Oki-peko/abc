A,B,C,D,E,F,X = map(int,input().split())
 
Td,Ad = 0,0

for i in range(X):
    if i % (A+C) < A:
        Td += B
    if i % (D+F) < D:
        Ad += E

if Td > Ad:
    print("Takahashi")
elif Td < Ad:
    print("Aoki")
else:
    print("Draw")