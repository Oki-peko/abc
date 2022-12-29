S = input()
ball = []
stack = []
now = -1

for i in range(len(S)):
  if S[i] in ball:
    print("No")
    exit()
  
  ball.append(S[i])
  
  if now >= 0:
    if S[i] == "(":
      now += 1
      stack.append([])
    elif S[i] == ")":
      for x in stack[now]:
        ball.remove(x)
      now -= 1
    else:
      stack[now].append(S[i])

print("Yes")