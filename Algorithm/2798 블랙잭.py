N, M = map(int, input().split())
S=list(map(int, input().split()))
result=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if S[i]+S[j]+S[k] >M:
                continue
            else:
                result=max(result,S[i]+S[j]+S[k])

print(result)