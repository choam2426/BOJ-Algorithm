m=int(input())
n=int(input())
s_list=[]
if m==1:
    m+=1
for i in range(m,n+1):
    no=0
    for j in range(2,i):
        if i%j==0:
            no+=1
    if no == 0:
        s_list.append(i)
if len(s_list) == 0:
    print(-1)
else:
    print(sum(s_list))
    print(s_list[0])