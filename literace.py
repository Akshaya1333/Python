# cook your dish here
t=int(input())
for i in range(t):
    p,l=map(int,input().split())
    if((l/p)>=0.75):
        print('yes')
    else:
        print('no')
