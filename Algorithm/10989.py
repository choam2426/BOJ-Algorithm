import sys

N=int(sys.stdin.readline())
li=[0]*10000

for i in range(N):
    num=int(sys.stdin.readline())
    li[num-1]+=1

for i in range(10000):
    if li[i] != 0:
        for j in range(li[i]):
            print(i+1)