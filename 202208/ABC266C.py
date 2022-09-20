import math
import numpy as np

A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())
C1,C2 = map(int,input().split())
D1,D2 = map(int,input().split())

def cul_angle(x0,y0,x1,y1,x2,y2):
    #２次元空間の場合
    #角度の中心位置
    x0,y0=A1,A2
    #方向指定1
    x1,y1=B1,B2
    #方向指定2
    x2,y2=C1,C2

    #角度計算開始
    vec1=[x1-x0,y1-y0]
    vec2=[x2-x0,y2-y0]
    absvec1=np.linalg.norm(vec1)
    absvec2=np.linalg.norm(vec2)
    inner=np.inner(vec1,vec2)
    cos_theta=inner/(absvec1*absvec2)
    theta=math.degrees(math.acos(cos_theta))
    print('angle='+str(round(theta,2))+'deg')