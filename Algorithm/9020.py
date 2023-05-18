def num(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

TC=int(input())
for i in range(TC):
    n=int(input())
    b=int(n/2)
    while True:
        if num(b)&num(n-b):
            print(n-b, b)
            break
        b+=1
