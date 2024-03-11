N = int(input())
A = list(map(int, input().split()))

tmp = 1
new_A = []

for i in range(N):
    if i < N // 2 + 1:
        if A[i] >= tmp:
            new_A.append(tmp)
        else:
            new_A.append(A[i])
    else:
        if A[-(i - N // 2 + 1)] >= tmp:
            new_A.append(tmp)
        else:
            new_A.append(A[-(i - N // 2 + 1)])
    tmp += 1

print(new_A[len(new_A) // 2])
