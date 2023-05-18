number = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N, B = input().split()
N = list(N)
B = int(B)
result = 0
for i in range(len(N)):
    result += number.index(N[(i+1)*-1])*(B**i)
print(result)
