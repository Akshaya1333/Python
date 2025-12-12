# cook your dish here
for _ in range(int(input())):
    w,p,k=map(int,input().split())
    if k<w :
        print(k*2)
    # elif w==0 :
    #     print(k)
    # elif p==0:
    #     print(k*2)
    else:
        print(w*2 + (k-w))
