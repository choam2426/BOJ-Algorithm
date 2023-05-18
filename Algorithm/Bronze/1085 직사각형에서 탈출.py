S1=list(map(int,input().split()))
S2=[]
S2[:2]=S1[:2]
S2.append(S1[2]-S1[0])
S2.append(S1[3]-S1[1])
print(min(S2))