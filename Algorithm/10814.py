N=int(input())
S=[]
for i in range(N):
    [a, b]=map(str,input().split())
    S.append(list([int(a),b]))
    S[i].insert(1,i)

S.sort()

for i in range(N):
    print(S[i][0],S[i][2])