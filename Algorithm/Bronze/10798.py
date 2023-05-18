arr = []
for _ in range(5):
    arr.append(list(input()))
i = 0
while True:
    a = 0
    for j in range(5):
        try:
            if arr[j][i]:
                print(arr[j][i], end='')
        except:
            a += 1
            pass
    i += 1
    if a == 5:
        break
