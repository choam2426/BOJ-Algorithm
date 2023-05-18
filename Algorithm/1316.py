N = int(input())
cnt = 0
for _ in range(N):
    s = list(input())
    chk = []
    for j in range(len(s)):
        if not s[j] in chk:
            chk.append(s[j])
        else:
            if s[j] == chk[j-1]:
                chk.append(s[j])
            else:
                break
    else:
        cnt += 1
print(cnt)
