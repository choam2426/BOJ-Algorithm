Test_Case=int(input())
for i in range(Test_Case):
    k=int(input())
    n=int(input())
    a=list(range(1,n+1))
    for j in range(k):
        for h in range(n-1):
            a[h+1]+=a[h]
    print(a[n-1])