from itertools import combinations

h = [int(input()) for _ in range(9)]

for i in combinations(h, 7): #h에서 7개를 뽑는 조합
    if sum(i)==100:
        for j in sorted(i):
            print(j)
        break
