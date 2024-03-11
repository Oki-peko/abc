S = list(input())

flg = True
ans = ""

for i in S:
    if i == "|":
        if flg == True:
            flg = False
        else:
            flg = True
        continue
    
    if flg == True:
        ans += i

print(ans)