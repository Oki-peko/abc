h, w = map(int, input().split())
r, c = map(int, input().split())

result = 4
if h == r:
    result -= 1
if w == c:
    result -= 1
if r == 1:
    result -= 1
if c == 1:
    result -= 1

print(result)