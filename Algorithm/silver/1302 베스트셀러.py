book=dict()

for _ in range(int(input())):
    b=input()
    if b in book:
        book[b]+=1
    else:
        book[b]=1

m=max(book.values())
best=[]
for k, v in book.items():
    if v == m :
        best.append(k)

best.sort()
print(best[0])
