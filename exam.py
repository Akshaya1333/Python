x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    s=a*b 
    h=s/2
    if c>h:
        print("yes")
    else:
        print("no")
