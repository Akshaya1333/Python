import math
hlo=int(input())
for love in range(hlo):
    lv1,lv2=map(int,input().split())
    if lv1/lv2<1:
        print("0")
    else:
        print(math.ceil((lv1-lv2)/4))
