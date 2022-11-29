N = int(input())
A = [0]+list(map(int,input().split()))
Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        A = [query[1]]*N
    if query[0] == 2:
        A[query[1]]+=query[2]
    if query[0] == 3:
        print(query[1])