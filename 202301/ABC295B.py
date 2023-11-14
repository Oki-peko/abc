R,C = map(int,input().split())

map = [list(input()) for _ in range(C)]

for x in range(C):
  for y in range(R):
    if map[x][y].isdigit():
        bomb = int(map[x][y])
        for i in range(C):
            for j in range(R):
                if abs(x - i) + abs(y - j) <= bomb:
                    if not map[i][j].isdigit():
                        map[i][j] = "."

for ans in map:
    print(*ans,sep="")