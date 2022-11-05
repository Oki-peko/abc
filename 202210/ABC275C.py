S = [input() for _ in range(9)]
ans = 0

for y in range(8):
    for x in range(8):
        if S[y][x] == "#":
            for l in range(1,9):
                if 1 <= y+l <= 8 and 1 <= x+l <= 8:
                    if S[y][x+l] == "#" and S[y+l][x] == "#" and S[y+l][x+l] == "#":
                        ans += 1

for y in range(1,8):
    for x in range(1,8):
        for l in range(1,5):
            if 0 <= y+l <= 8 and 0 <= x+l <= 8 and 0 <= x-l <= 8 and 0 <= y-l <= 8:
                if S[y][x+l] == "#" and S[y][x-l] == "#" and S[y+l][x] == "#" and S[y-l][x] == "#":
                    ans += 1

print(ans)