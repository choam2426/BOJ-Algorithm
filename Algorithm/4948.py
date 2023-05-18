from ast import While


all=[]
for i in range(2,246913):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        all.append(i)

while True:
    a=int(input())
    count=0
    if a==0:
        break
    for i in all:
        if a<i<=2*a:
            count+=1
    print(count)
