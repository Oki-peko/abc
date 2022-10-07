N = int(input())
s,t = [],[]
a = []

for i in range(N):
    tmp = input().split()
    s.append(tmp[0])
    t.append(tmp[1])

    if s[i] in a and t[i] in a:
        print("No")
        exit()

    if not s[i] in a:
        a.append(s[i])
    if not t[i] in a:
        a.append(t[i])

a = []

for i in reversed(range(N)):
    if s[i] in a and t[i] in a:
        print("No")
        exit()

    if not s[i] in a:
        a.append(s[i])
    if not t[i] in a:
        a.append(t[i])

print("Yes")