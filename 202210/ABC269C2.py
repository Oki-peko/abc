N = int(input())
ans = []

i = N
while i >= 0:
    i = N & i
    ans.append(i)
    i -= 1

print(*sorted(ans),sep="\n")