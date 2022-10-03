ans = str(hex(int(input())))[2:]
if len(ans) == 1:
  ans = "0"+ans
print(ans.upper())