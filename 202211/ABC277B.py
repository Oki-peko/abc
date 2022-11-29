N = int(input())
S = [input() for _ in range(N)]
tmp = []

for i in S:
    if i in tmp:
        print("No")
        exit()
    if i[0] not in ["H","D","C","S"]:
        print("No")
        exit()
    elif i[1] not in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
        print("No")
        exit()
    
    tmp.append(i)

print("Yes")
