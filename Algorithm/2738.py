N, M = map(int,input().split())
arr1=[]
arr2=[]
for i in range(N):
    a=list(map(int,input().split()))
    arr1.append(a)

for i in range(N):
    a=list(map(int,input().split()))
    arr2.append(a)

for i in range(N):
    for j in range(M):
        arr1[i][j]=arr1[i][j]+arr2[i][j]

for i in range(N):
    for j in range(M):
        print(arr1[i][j], end=" ")
    print()