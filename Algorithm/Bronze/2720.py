T = int(input())
coin = [25, 10, 5, 1]
for i in range(T):
    change = []
    n = int(input())
    for j in range(4):
        if n >= coin[j]:
            change.append(n // coin[j])
            n = n % coin[j]
        else:
            change.append(0)
        print(change[j], end=" ")
