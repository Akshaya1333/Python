import math
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a<=3:
        print(a*b)
    else:
        if (a%3==0):
            print((a*b)+math.trunc((a/3-1)*c))
        else:
            m=(int(a/3))*c+(a*b)
            print(m)
