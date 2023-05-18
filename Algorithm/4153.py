while True:
    a=list(map(int,input().split()))
    if sum(a)==0:
        break
    for i in range(3):
        a[i]=a[i]**2
    b=max(a)
    c=sum(a)-max(a)
    if c==b:
        print('right')
    else:
        print('wrong')