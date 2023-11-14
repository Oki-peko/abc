def find_cycle(n, adj):
    color = [0]*n
    path = [0]*n
    cycle = []
    found = False
    
    def dfs(v):
        nonlocal found
        color[v] = 1
        for to in adj[v]:
            if color[to] == 0:
                path[to] = v
                dfs(to)
            elif color[to] == 1:
                nonlocal cycle
                cycle = [to]
                p = v
                while p != to:
                    cycle.append(p)
                    p = path[p]
                cycle.append(to)
                found = True
        color[v] = 2
        if found:
            return
    
    for i in range(n):
        if color[i] == 0:
            dfs(i)
            if found:
                return cycle[::-1]
    
    return None

# Main Function
N = int(input())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for i in range(N):
    A[i] -= 1  # Assuming the nodes are numbered from 1 to N in input
    adj[i].append(A[i])

cycle = find_cycle(N, adj)

if cycle is None:
    print("No cycle found.")
else:
    cycle = [i+1 for i in cycle]  # Converting back to 1-indexed
    print("Cycle found: ", cycle)
