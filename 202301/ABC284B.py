N = int(input())
S = input()

for dif in range(1,N):
    for i in range(1,N+1):
        if i + dif > N:
            print(i-1)
            break
        if S[i-1] == S[dif+i-1]:
            print(i-1)
            break