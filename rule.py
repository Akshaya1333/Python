x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    s=107/100
    if a*s>=b:
        print("YES")
    else:
        print("NO")
