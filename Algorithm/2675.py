TC = int(input())
S=[]
for i in range(TC):
    S.append(list(map(str,input())))
for j in range(TC):
    for k in S[j][2:]:
        print(k*int(S[j][0]),end="")
    print()