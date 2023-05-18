import sys
N = int(input())
S1 = list(map(int, sys.stdin.readline().split()))
M = int(input())
S2 = list(map(int, sys.stdin.readline().split()))
S1.sort()

for i in S2:
    ft=0
    lt=len(S1)-1
    flag=True
    while ft<=lt:
        mt = (ft+lt)//2
        if S1[mt]==i:
            print(1)
            flag=False
            break
        elif S1[mt]>i:
            lt=mt-1
        else :
            ft=mt+1
    if flag:
        print(0)