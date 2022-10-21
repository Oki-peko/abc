N = int(input())
A = list(map(int,input().split()))

arr = [0]*2001

for i in A:
    arr[i] = 1

ans = 0
for i in arr:
    if i == 0:
        print(ans)
        exit()
    else:
        ans += 1