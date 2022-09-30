S = input()
listS = [S[x] for x in range(len(S))]
flg = True

if S.isupper():
    flg = False
elif S.islower():
    flg = False
elif len(listS) != len(set(listS)):
    flg = False

if flg == True:
    print("Yes")
else:
    print("No")