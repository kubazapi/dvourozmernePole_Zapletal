matrix = [
    [1, 2, 3],
    [4, 105, 6],
    [7, 8, 9]
]

matrix.append([10, 11, 12])

for row in matrix:
    row.append(0) 

for row in matrix:
    print(row)
