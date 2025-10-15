
T = int(input())
for i in range(T):
    x, y, z = map(int, input().split())
    c = z-y
    print(c//x)
