S = input()
# dream dreamer erase eraser
while True:
    if S == "":
        print("YES")
        exit()
    elif S[-5:] == "dream":
        S = S[:-5]
    elif S[-7:] == "dreamer":
        S = S[:-7]
    elif S[-5:] == "erase":
        S = S[:-5]
    elif S[-6:] == "eraser":
        S = S[:-6]
    else:
        print("NO")
        exit()