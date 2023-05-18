T_C=int(input())
for i in range(T_C):
    a,b,c=map(int,input().split())
    if c%a==0:
        floor=int(c/a)
        r_n=a
    else:
        floor=int(c/a)+1
        r_n=c%a
    print(r_n*100+floor)