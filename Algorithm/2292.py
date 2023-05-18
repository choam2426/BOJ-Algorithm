num=int(input())
i=2
room_num=8
if num==1:
    print(1)
elif 0<num<8:
    print(2)
else:
    while True:
        room_num+=i*6
        if num<=room_num-1:
            print(i+1)
            break
        i+=1