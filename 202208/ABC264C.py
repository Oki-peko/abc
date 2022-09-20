import itertools

H1,W1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H1)]
H2,W2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H2)]

ptn_H = []
con_H = itertools.combinations(range(1,H1+1), H2)
for v in con_H:
    ptn_H.append(v)

ptn_W = []
con_W = itertools.combinations(range(1,W1+1), W2)
for v in con_W:
    ptn_W.append(v)

for i in ptn_H:
    for j in ptn_W:
        for k in range(H2):
            for l in range(W2):
                if B[k][l] != A[i[k]-1][j[l]-1]:
                    flg = False
                    break
                else:
                    flg = True
        if flg == True:
            print("Yes")
            exit()

print("No")