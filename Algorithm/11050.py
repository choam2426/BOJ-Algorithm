N, K = map(int, input().split())
k = 1
n = 1
a = 1
A = N-K
if K == 0 or K == 1:
    pass
else:
    for i in range(2, K+1):
        k = k*i
for i in range(2, N+1):
    n = n*i
if A == 0 or A == 1:
    pass
else:
    for i in range(2, A+1):
        a = a*i
print(int(n/(k*a)))
