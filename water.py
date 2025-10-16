x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if (a+c*d)>b:
        print("overFlow")
    elif (a+c*d)<b:
        print("Unfilled")
    else:
        print("filled")
