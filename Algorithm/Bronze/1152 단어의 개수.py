S = list(map(str,input()))
if S[0] == " ":
    del S[0]

if S[-1] == " ":
    del S[-1]

shift = S.count(" ")
a=list(set(S))
if len(a) == 1:
    if a.find(" ") ==-1:
        print(1)
    else:
        print(0)
elif shift == 0:
    print(1)
else:
    print(shift+1)