import sys
import heapq as hq

input = sys.stdin.readline
arr=[]
n=int(input())

for _ in range(n):
    x=int(input())
    if x:
        hq.heappush(arr, (abs(x), x))
    else:
            print(hq.heappop(arr)[1] if arr else 0)