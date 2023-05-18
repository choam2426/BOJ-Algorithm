arr1=[]
index=-1
M,N=0,0

for i in range(9):
    a=list(map(int,input().split()))
    arr1.append(a)


for i in range(9):
    for j in range(9):
        if arr1[i][j]>index:
            index=arr1[i][j]
            M=i
            N=j

print(index, "\n",M+1," ",N+1)
