x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    print(a+((d*b)-(c*d)))
