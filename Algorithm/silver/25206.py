score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

grade = [0.0, 0.0]

for _ in range(20):

    arr = list(input().split())

    if arr[2] == 'P':
        pass
    else:
        grade[0] += float(arr[1])

        grade[1] += float(arr[1])*score[arr[2]]


print(round(grade[1]/grade[0], 6) if grade[1] != 0.0 else '0.000000')
