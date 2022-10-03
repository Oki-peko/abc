N = int(input())
a = list(map(int,input().split()))

now = 0
for i in range(len(a)):
    now += 1
    if a[i] < now:
        a.append(a.pop(now-1))
    if a[i] != now:
        if len(a) >= now+1:
            a.pop()
            a.pop()
            a.insert(now-1,now)
        else:
            break

cnt = 0
a += [-1]
for i in range(len(a)):
    if a[i] != cnt+1:
        print(cnt)
        break
    cnt += 1
