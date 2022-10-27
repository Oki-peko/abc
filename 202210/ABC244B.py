N = int(input())
T = input()
X,Y = 0,0

dir = 0
dir_X = [1,0,-1,0]
dir_Y = [0,-1,0,1]

for i in range(N):
    if T[i] == "R":
        dir += 1
    else:
        X += dir_X[dir%4]
        Y += dir_Y[dir%4]

print(X,Y)