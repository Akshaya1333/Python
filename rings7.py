# cook your dish here
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=b*c
    e=str(d)
    f=len(e)
    if f==5:
        print("YES")
    else:
        print("NO")
