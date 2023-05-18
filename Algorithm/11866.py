N, K = map(int, input().split())
S = []
Y = []
a = -1
for i in range(1, N+1):
    S.append(i)

for i in range(N):
    for j in range(K):
        a += 1
        if a == len(S):
            a = 0
    Y.append(S[a])
    del S[a]
    a -= 1
a = 0
print("<", end="")
for i in Y:
    a += 1
    if a < len(Y):
        print(i, end=", ")
    else:
        print(i, end="")
print(">")
