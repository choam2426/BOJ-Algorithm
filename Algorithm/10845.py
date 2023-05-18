import sys
t_c=int(sys.stdin.readline())
queue=[]
for i in range(t_c):
    order=list(map(str,sys.stdin.readline().split()))
    if order[0]=='push':
        queue.append(int(order[1]))
    elif order[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif order[0]=='size':
        print(len(queue))
    elif order[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif order[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif order[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])