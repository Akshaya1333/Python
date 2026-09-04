arr = tuple(map(int, input().split()))
x = int(input())
i=0
for i in range(0,len(arr)):
    if x==arr[i]:
        print(i)
        break
