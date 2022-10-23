A,B = map(int,input().split())
if A == B:
    print("1.000")
else:
    print("0." + str(int((B/A+0.0005)*1000)).zfill(3))