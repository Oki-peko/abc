def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

N = base10int(int(input()),2)
cnt = str(N).count("1")

list_1 = []

for i in range(len(N)):
  if N[len(N)-i-1] == "1":
    list_1.append(i)

list_1.reverse()

for i in range(cnt):
  for j in range(cnt):
    N = 0

a = []
for bit in range(1 << cnt):
    b = []
    for i in range(cnt):
        if (bit & (1 << i)):
            b.append('１')
        else:
            b.append('0')
    a.append("".join(b))

ans = [0] 

for i in a:
  tmp = 0
  for j in range(cnt):
    if i[j] == "1":
      tmp += 2 ** list_1[j]
  ans.append(tmp)

print(ans)
print(list_1)