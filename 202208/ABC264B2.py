R,C = map(int,input().split())

if (abs(max(R,C)-8) % 2 == 0):
    print("black")
else:
    print("white")