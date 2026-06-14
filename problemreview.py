n=int(input())
for i in range(n):
    a=int(input())
    b=map(int,input().split())
    c=min(b)
    if c>4:
        print("YES")
    else:
        print("NO")
