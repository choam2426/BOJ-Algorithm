a = set(range(1,10001))
b = set()

for i in range(1,10001):
    for j in str(i):
       i+=int(j)
    b.add(i)

d=sorted(a-b) #sorted=정렬함수
print(b)
for k in d:
    print(k)
