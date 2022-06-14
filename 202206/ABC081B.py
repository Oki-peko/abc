# https://atcoder.jp/contests/abs/tasks/abc081_b

N = int(input())
A = list(map(int, input().split()))
tmp = A.copy()
cnt = 0
flg = True

while flg == True:
  for i in range(N):
    if tmp[i] % 2 == 0:
      tmp[i] //= 2
    else:
      print(cnt)
      flg = False
      break
  cnt += 1