S=input()
S2=[]
for i in str(S):
    S2.append(int(i))
S2.sort(reverse=True)
for i in range(len(S2)):
    print(S2[i], end="")