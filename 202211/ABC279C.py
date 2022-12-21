H,W = map(int,input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

S_t = []
T_t = []

for j in range(W):
    tmp_S = []
    tmp_T = []
    for i in range(H):
        tmp_S.append(S[i][j])
        tmp_T.append(T[i][j])
    S_t.append(tmp_S)
    T_t.append(tmp_T)

S_t.sort()
T_t.sort()

print(S_t)
print(T_t)

if S_t == T_t:
    print("Yes")
else:
    print("No")