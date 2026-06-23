t=int(input())
for i in range(t):
     x,y,d=map(int,input().split())
     c=x-y
     if c<0:
         c=-(c)
     if c<=d:
         print("YES")
     else:
         print("NO")
