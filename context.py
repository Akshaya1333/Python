# cook your dish here
t = int(input())

for _ in range(t):
    X, Y = map(int, input().split())
    
    alice = (X + Y) // 2
    bob = Y - alice
    
    print(alice, bob)
