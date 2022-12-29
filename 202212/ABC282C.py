N = int(input())
S = input()

ans = []
flg = False

for i in range(N):
    if S[i] == "\"":
        if flg == True:
            flg = False
        else:
            flg = True
    if S[i] == "," and flg == False:
        ans.append(".")
    else:
        ans.append(S[i])

print(''.join(ans))
