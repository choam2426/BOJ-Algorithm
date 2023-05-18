N=int(input())
S=[]
for i in range(N):
    s=(input())
    S.append([len(s), s])
S=list(set([tuple(S)for S in S]))
S.sort()
for i in range(len(S)):
    print(S[i][1])