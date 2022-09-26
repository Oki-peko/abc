N,X,Y,Z = map(int,input().split())
A = list(enumerate(map(int,input().split()),1))
B = list(enumerate(map(int,input().split()),1))
AB = list(enumerate([x+y for ((i,x),(j,y)) in zip(A,B)],1))

ok = []

max = 0
count = 0
sort_A = sorted(A,key=lambda x:x[1],reverse=True)
for score in sort_A:
    if count < X:
        ok.append(score[0])
        count += 1

max = 0
count = 0
sort_B = sorted(B,key=lambda x:x[1],reverse=True)
for score in sort_B:
    if count < Y:
        if score[0] not in ok:
            ok.append(score[0])
            count += 1

max = 0
count = 0
sort_AB = sorted(AB,key=lambda x:x[1],reverse=True)
for score in sort_AB:
    if count < Z:
        if score[0] not in ok:
            ok.append(score[0])
            count += 1

ok.sort()
print(*ok,sep='\n')