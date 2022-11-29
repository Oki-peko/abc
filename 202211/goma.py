h,m = input().split()
h = str(h).zfill(2)
m = str(m).zfill(2)
if h == '0':
    h = '00'
if m == '0':
    m = '00'
org_h = h[0] + h[1]
org_m = m[0] + m[1]
flg = False
 
while flg != True:
    new_h = int(org_h[0] + org_m[0])
    new_m = int(org_h[1] + org_m[1])
    
    if new_h < 24 and new_m < 60:
        ans_h = org_h
        ans_m = org_m
        flg = True
        break
    else:
        if org_m == '59':
            org_h = str(int(org_h) + 1)
            if int(org_h) == 24:
                org_h = '00'
            org_m = '0'
            str(org_h).zfill(2)
            str(org_m).zfill(2)
            if org_h == '0':
                org_h = '00'
            if org_m == '0':
                org_m = '00'
        else:
            org_m = str(int(org_m) + 1)
            str(org_h).zfill(2)
            str(org_m).zfill(2)
            if org_h == '0':
                org_h = '00'
            if org_m == '0':
                org_m = '00'

if flg == True:
     print(ans_h, ans_m)