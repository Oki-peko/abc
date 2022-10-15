N = int(input())
s, t = [], []
for i in range(N):
  u, v = input().split()
  s.append(u)
  t.append(v)

for i in range(N):
    s_flg = True
    t_flg = True
    for j in range(N):
        if i != j:
            if s[i] == s[j] or s[i] == t[j]:
                s_flg = False
            if t[i] == s[j] or t[i] == t[j]:
                t_flg = False
        if s_flg == False and t_flg == False:
            print("No")
            exit()

print("Yes")
