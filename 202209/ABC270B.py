X,Y,Z = map(int,input().split())

for _ in range(2):
    if 0 < X < Y:
        print(X)
    elif 0 < Z < Y < X:
        print(X)
    elif Y < 0 < X:
        print(X)
    elif Z < 0 < Y < X:
        print(abs(Z*2) + X)
    elif 0 < Y < X < Z:
        print("-1")
    
    X,Y,Z = -X,-Y,-Z