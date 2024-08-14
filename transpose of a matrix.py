a = [[1, 2], [3, 4]]
transpose_a = [[a[j][i]
for j in range(len(a))]
for i in range(len(a[0]))]
print("Original matrix:")
for row in a:
    print(row)
print("\nTransposed matrix:")
for row in transpose_a:
    print(row)
