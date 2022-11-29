import math

A,B = map(int,input().split())
flg = True
ans = A
g = 0
while flg == True:
    tmp = g * B + (A / math.sqrt(g+1))
    if tmp <= ans:
        ans = tmp
        g += 1
    else:
        print(ans)
        exit()