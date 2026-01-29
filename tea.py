n=int(input())
for i in range(n):
    x,y,z=map(int,input().split())
    print((z*x)//y) if x%y==0 else print(((x//y)+1)*z)
