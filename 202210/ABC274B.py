X,K = map(int,input().split())
ans = X

for i in range(K+1):
    dev = ans // (10 ** i)
    left = (ans % (10 ** i)) //  (10 ** (i-1))

    if left >= 5:
        dev += 1

    ans = dev * (10 ** i)

print(ans)