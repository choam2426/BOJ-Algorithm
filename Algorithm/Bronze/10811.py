N, M = map(int, input().split())

basket = []

for l in range(N):
    basket.append(l+1)

for _ in range(M):
    i, j = map(int, input().split())
    if i == j:
        pass
    else:
        l1 = []
        for k in range(j, i-1, -1):
            l1.append(basket[k-1])
        for l in range(i-1, j):
            basket[l] = l1.pop(0)


for k in range(N):
    print(basket[k], end=" ")
