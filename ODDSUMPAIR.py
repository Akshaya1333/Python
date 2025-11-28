t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a+b) % 2 == 1 or (b+c) % 2 == 1 or (a+c) % 2 == 1:
        print("yes")
    else:
        print("no")
