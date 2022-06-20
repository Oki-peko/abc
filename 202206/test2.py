import math
N,K = map(int,input().split())
A = list(map(int,input().split()))

XY_LIST = []
min_list =[1000000]*N

for _ in range(N):
  XY_LIST.append(list(map(int,input().split())))

for i in range(N):
    for j in A:
        dst = math.sqrt((XY_LIST[i][0]-XY_LIST[j-1][0])**2+(XY_LIST[i][1]-XY_LIST[j-1][1])**2)
        if dst < min_list[i]:
            min_list[i] = dst

print(max(min_list))