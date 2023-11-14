N, Q = map(int, input().split())
wait_dict = {}
count = 0

for _ in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        count += 1
        wait_dict[count] = count
    elif event[0] == 2:
        del wait_dict[event[1]]
    else:
        first_key = next(iter(wait_dict))
        first_value = wait_dict[first_key]
        print(first_value)