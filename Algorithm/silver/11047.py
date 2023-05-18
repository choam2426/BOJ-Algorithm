import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin_value = []
coin_num = 0

for i in range(N):
    a = int(input())
    if K >= a:
        coin_value.append(a)
    else:
        pass

for i in range(len(coin_value)-1, -1, -1):
    b = 0
    if K >= coin_value[i]:
        b = K // coin_value[i]
        K -= coin_value[i]*b
        coin_num += b
    elif K == 0:
        break

print(coin_num)
