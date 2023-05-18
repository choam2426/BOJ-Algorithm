while True:
    S=input()
    a1=[]
    a2=[]
    if S=='0':
        break
    for i in S:
        a1.append(i)
        a2.insert(0,i)
    print(a1,a2)
    if a1==a2:
        print('yes')
    else:
        print('no')