N = int(input())
dic = {}

for _ in range(N):
    S = input()
    if S not in dic:
        dic[S] = 0
        print(S)
    else:
        dic[S] += 1
        print(S+"("+str(dic[S])+")")