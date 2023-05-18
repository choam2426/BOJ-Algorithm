a, b = map(int, input().split())
l = [0]*a
for _ in range(b):
    st, lt, bn = map(int, input().split())
    for i in range(st,lt+1):
        l[i-1]=bn

for i in range(a):
    print(l[i], end=" ")