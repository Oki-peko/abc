N,T = map(int,input().split())
A = list(map(int,input().split()))

sumA = sum(A)
now = T % sumA

cnt = 1

for i in A:
    if now - i < 0:
        print(cnt,now)
        exit()
    else:
        cnt += 1
        now -= i
