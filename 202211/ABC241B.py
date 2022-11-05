N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in B:
    if i in A:
        A.remove(i)
    else:
        print("No")
        exit()

print("Yes")