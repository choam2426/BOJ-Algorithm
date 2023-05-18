from collections import Counter
import sys
input=sys.stdin.readline
N=int(input())
S=[]
for i in range(N):
    S.append(int(input()))

S.sort()

print(round(sum(S)/len(S)))

print(S[len(S)//2])

f = Counter(S)
b = f.most_common()
if len(S) >1: 
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(S[0])

print(S[-1]-S[0])