N,Q = map(int,input().split())
L = []
for _ in range(N):
    L.append(list(map(int,input().split())))
s,t = [],[]
for _ in range(Q):
    tmp_s,tmp_t = map(int,input().split())
    s.append(tmp_s)
    t.append(tmp_t)

for i in range(Q):
    print(L[s[i]-1][t[i]])
