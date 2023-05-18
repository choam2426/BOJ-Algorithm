obj=[1,1,2,2,2,8]

now_obj=list(map(int,input().split()))

for i in range(6):
    print(obj[i]-now_obj[i], end=' ')