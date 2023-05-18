'''sugar=int(input())
bag=sugar//5
if sugar==4 or sugar==7:
    print(-1)
else:
    sugar=sugar%5
    if sugar==0:
        print(bag)
    elif sugar==1:
        print(bag+1)
    elif sugar==2:
        print(bag+2)
    elif sugar==3:
        print(bag+1)
    elif sugar==4:
        print(bag+2)'''

sugar=int(input())
bag=0
while sugar>=0:
    if sugar % 5==0:
        bag+=sugar/5
        print(int(bag))
        break
    sugar-=3
    bag+=1
else:
    print(-1)