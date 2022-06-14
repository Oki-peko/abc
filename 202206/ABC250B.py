n, a, b = map(int, input().split())
 
row = ""
 
for i in range(n):
    if i % 2 == 0:
        mark = "."
    else:
        mark = "#"
    
    row = ""

    for j in range(n):
        row += mark * b
        if mark == ".":
            mark = "#"
        else:
            mark = "."

    for k in range(a):
        print(row)