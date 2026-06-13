n=int(input())
for i in range(n):
    count=0
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for k in c:
        if k>=b:
            count+=1
    print(count)
