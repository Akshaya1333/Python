a=int(input())
for i in range(a):
    x,y,z=map(int,input().split())
    if x*z<y:
        print("yes")
    else:
        print("no")
