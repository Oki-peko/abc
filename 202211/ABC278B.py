H,M = map(int,input().split())
# A = H // 10  |A   C|
# B = H % 10   |  :  |
# C = M // 10  |B   D|
# D = M % 10

# likeH = (H // 10) * 10 + (M // 10)
# likeM = (H % 10) * 10 + (M % 10)

# if 0 <= likeH < 24 and 0 <= likeM < 60:
#         print(H,M)
#         exit()

for _ in range(24*60):
    likeH = (H // 10) * 10 + (M // 10)
    likeM = (H % 10) * 10 + (M % 10)

    if 0 <= likeH < 24 and 0 <= likeM < 60:
        print(H,M)
        exit()
    
    M += 1

    if M == 60:
        H += 1
        M = 0
    
    if H == 24:
        H = 0