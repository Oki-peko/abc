from math import atan2, cos, sin
 
A, B = map(int, input().split())
 
sin = sin(atan2(A, B))
cos = cos(atan2(A, B))
 
print(sin, cos)