A, B, C=map(int, input().split())
day = (C-B)/(A-B)
if day != int(day):
    day+=1
print(int(day))
