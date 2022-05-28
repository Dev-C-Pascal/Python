day_symb = ('*+ox-<' * 1000)
m = 0
subjects = []
while True:
    day = input()
    if day == '':
        break
    else:
        subjects.append(day.split(', '))
        m += 1
histogr = [str()] * len(subjects[0])
for i in range(m):
    for j in range(len(subjects[0])):
        histogr[j] = day_symb[i] * int(subjects[i][j]) + histogr[j]
histogr = [x.rjust(max(map(len, histogr)), ' ') for x in histogr]
for i in range(len(histogr[0])):
    [print(h[i] * 2, end=' ') for h in histogr]
    print()
