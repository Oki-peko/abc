H,W = map(int,input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

flg = True

for i in range(H):
    if S[i].count("#") != T[i].count("#"):
        flg = False
        break

if flg == True:
    print("Yes")
else:
    print("No")