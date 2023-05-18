board = [[False]*100 for _ in range(100)]
area = 0
for i in range(int(input())):
    wid, hei = map(int, input().split())
    for j in range(10):
        for k in range(10):
            board[wid+j][hei+k] = True
for i in range(100):
    area += board[i].count(True)
print(area)
