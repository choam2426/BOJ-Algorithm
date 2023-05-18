def so(a):
    for j in range(2,int((a**0.5)+1)):
        if a%j==0:
            break
    else:
        print(a)

m,n=map(int,input().split())
if m==1:
    m+=1
for i in range(m,n+1):
    so(i)
    #에라토스테네스의 체