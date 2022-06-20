N = int(input())
A_list = []

for i in range(N):  
  B_list = []
  for j in range(i+1):
    if j == 0 or j == i:
      B_list.append(1)
    else:
      B_list.append(A_list[i-1][j] + A_list[i-1][j-1])
  A_list.append(B_list)
  print(*B_list)