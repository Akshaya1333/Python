x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a==b==c==d==0:
        print("IN")
    else:
        print("OUT")
