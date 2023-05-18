number = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N, B = map(int, input().split())
result = []
ex = 0
while N-B**(ex+1) >= 0:
    ex += 1
for i in range(ex, -1, -1):
    if i == 0:
        result.append(number[N])
        break
    else:
        result.append(number[N//B**i])
        N = N % B**i
print("".join(result))
