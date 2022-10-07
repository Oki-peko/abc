a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

if a == c:
    x = e
if a == e:
    x = c
else:
    x = a

if b == d:
    y = f
if y== f:
    f = d
else:
    y = b

print(x,y)