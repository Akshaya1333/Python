n=int(input())
for i in range(n):
    a=int(input())
    if a<=10:
       print("Lower Double")
    elif a>10 and a<=15:
       print("Lower Single")
    elif a>15 and a<=25:
       print("Upper Double")
    else:
       print("Upper Single")
