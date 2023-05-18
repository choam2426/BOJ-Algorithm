S=list(map(int,input().split()))
a=0
for i in range(len(S)):
    a+=S[i]**2

print(a%10)