# Write a Python program which takes two digits m(row) and n(column) as input and generates a two-dimensional array. the element value in the i-th and j-th column of the array should be i*j.
row_num = int(input("Input Number of Rows: "))
col_num = int(input("Input Number of Columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)