N,Q = map(int,input().split())
follow = [[False] * (N+1) for _ in range(N+1)]

for i in range(Q):
    T,A,B = map(int,input().split())
    if T == 1:
        follow[A][B] = True
    if T == 2:
        follow[A][B] = False
    if T == 3:
        if follow[A][B] == True and follow[B][]:
            print("Yes")
        else:
            print("No")