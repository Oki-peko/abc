L1,R1,L2,R2 = map(int,input().split())
ans = min(R1,R2)-max(L1,L2)
print(max(ans,0))