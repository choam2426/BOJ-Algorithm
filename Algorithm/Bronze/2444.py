N = int(input())
space = list(range(N-1, -1, -1))
star = list(range(N))
for i in range(2*N-1):
    a = i if i <= N-1 else (i-(N-2))*-1
    print(" "*space[a], end="")
    print("*"*((star[a]+1)*2-1))

'''
0 1 2 3 4 - 2 - 3 - 4 - 5
0 1 2 3 4  5  6  7  8
'''
