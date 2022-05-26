matrix = [
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
[11, 3, 2, 3, 4, 5, 6, 7, 8, 9 ],
[0, 11, 2, 3, 4, 5, 6, 7, 8, 9 ],
[0, 1, 11, 3, 4, 5, 6, 7, 8, 9 ],
[0, 1, 2, 11, 4, 5, 6, 7, 8, 9 ],
[0, 1, 2, 3, 11, 5, 6, 7, 8, 9 ],
[0, 1, 2, 3, 4, 11, 6, 7, 8, 9 ],
[0, 1, 2, 3, 4, 5, 11, 7, 8, 9 ],
[0, 1, 2, 3, 4, 5, 6, 11, 8, 9 ],
[0, 1, 2, 3, 4, 5, 6, 7, 11, 7 ]]
trans_matrix = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        trans_matrix[i][j] = matrix[j][i]
for i in range(10):
    for j in range(10):
        if i == j:
            print(trans_matrix[i][j], end=' ')
print()
for i in range(10):
    for j in range(10):
        if i == j + 1:
            print(trans_matrix[i][j], end=' ')