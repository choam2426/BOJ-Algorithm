N, M = map(int, input().split())
basket = []
for l in range(N):
    basket.append(l+1)

for _ in range(M):
    i, j = map(int, input().split())
    if i != j:
        a=basket[j-1]
        basket[j-1]=basket[i-1]
        basket[i-1]=a

for k in range(N):
    print(basket[k], end=" ")