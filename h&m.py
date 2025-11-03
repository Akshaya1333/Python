N = int(input())
for _ in range(N):
    N,K = map(int,input().split())
    
    total = N*K
    H = total//60
    M = total % 60
    print(H,M)
