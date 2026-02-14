max_val = -1
row_idx = 0
col_idx = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_val:
            max_val = row[j]
            row_idx = i + 1
            col_idx = j + 1

print(max_val)
print(row_idx, col_idx)