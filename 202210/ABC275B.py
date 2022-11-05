A,B,C,D,E,F = map(int,input().split())

ans = A * B
ans %= 998244353
ans *= C
ans %= 998244353
ans = D * E
ans %= 998244353
ans *= F
ans %= 998244353

MOD = 1000000007
a = 1111111111
b = 1234567890
c = 9876543210
print (a * b * c % MOD)
print (a * b % MOD * c % MOD)
print (a % MOD * b % MOD * c % MOD)