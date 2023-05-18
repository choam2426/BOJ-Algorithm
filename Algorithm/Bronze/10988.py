S1 = list(input())
S2 = list(S1)
S1.reverse()

for i in range(len(S1)):
    if S1[i] != S2[i]:
        print(0)
        break
else:
    print(1)
