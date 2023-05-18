tc = int(input())
for _ in range(tc):
    s = list(input())
    i = 0
    while 1:
        if s[i] != s[i+1] and s[i] == '(':
            del s[i+1]
            del s[i]
            i = -1
        i += 1
        if i == len(s)-1 or len(s) == 0:
            break
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
