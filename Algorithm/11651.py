import sys
input=sys.stdin.readline
N=(int(input()))
S1=[]
for i in range(N):
    a, b=(map(int,input().split()))
    S1.append([b,a])

S1.sort()
for i in range(N):
    print(S1[i][1],S1[i][0])