T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for weight in A:
        if X <= weight <= Y:
            count += 1
    print(count)
