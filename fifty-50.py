for i in range(int(input())):
    a,b=map(int,input().split())
    if(a<50):
        print("Z")
    elif(a>=50 and b<50):
        print("F")
    else:
        print("A")
