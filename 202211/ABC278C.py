N,Q = map(int,input().split())
dict = {}

for _ in range(Q):
    T,A,B = map(int,input().split())
    follow = str(A) + "to" + str(B)
    fol_back = str(B) + "to" + str(A)
    if T == 1:
        dict[follow] = True
    if T == 2:
        if follow in dict:
            del dict[follow]
    if T == 3:
        if follow in dict and fol_back in dict:
            print("Yes")
        else:
            print("No")