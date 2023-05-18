S = list(input().split())
A=list(map(int,(S[0])))
B=list(map(int,(S[1])))
a=0
b=0
for i in range(3):
   a+=A[i]*(10**i)
for i in range(3):
   b+=B[i]*(10**i)

if a>b:
    print(a)
else:
    print(b)

    #[::-1] 역순 연산자