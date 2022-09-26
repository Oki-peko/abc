N,X,Y = map(int,input().split())

UV = []
for _ in range(N-1):
  UV.append(list(map(int,input().split())))

root = [""]*100000
now = X
root[now] = str(now)

for _ in range(100000):
  for i in range(N-1):
    if UV[i][0] == now:
      now = UV[i][1]
      root[now] += " " + str(now)
    elif UV[i][1] == now:
      now = UV[i][0]
      root[now] += " " + str(now)
    
    if now == Y:
        print(root[now])
        exit()
