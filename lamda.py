# cook your dish here
n, m = map(int, input().split())

ls = [1] * n 
i = 0
m -= n

while m > 0:
    ls[i%n] += 1
    i += 1
    m -= 1
    
print(len(list(filter(lambda x: x >= 2, ls))))
