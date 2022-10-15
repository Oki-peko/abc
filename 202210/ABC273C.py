N = int(input())
A = list(map(int,input().split()))

even_max1 = 0
even_max2 = 0
odd_max1 = 0
odd_max2 = 0

for i in range(N):
    if A[i]%2==0:
        if even_max1 < A[i]:
            even_max1,even_max2 = A[i],even_max1
        elif even_max2 < A[i]:
            even_max2 = A[i]
    else:
        if odd_max1 < A[i]:
            odd_max1,odd_max2 = A[i],odd_max1
        elif odd_max2 < A[i]:
            odd_max2 = A[i]

if N == 2 and (A[0] + A[1]) % 2 != 0:
    print(-1)
else:
    print(max(even_max1+even_max2,odd_max1+odd_max2))