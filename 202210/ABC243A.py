V,A,B,C = map(int,input().split())
shampoo = [A,B,C]
ans=["F","M","T"]
turn = 0

while True:
    V -= shampoo[turn%3]
    if V < 0:
        print(ans[turn%3])
        exit()
    turn += 1