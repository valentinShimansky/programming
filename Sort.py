import random

def sum_string(m):
    result = []
    s = 0
    for i in range(len(m)):
        for j in range(len(m)):
            s += m[i][j]
        result.append(s)
        s = 0
    return result

def sort(l):
    for i in range(len(l)):
        curr = l[i]
        j = i - 1
        while j >= 0 and curr < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = curr
    return l

def transpose(list):
    result = [[ 0 for j in range (len(list))] for i in range (len(list))]
    for i in range(len(list)):
        for j in range(len(list[i])):
            result[i][j] = list[j][i]
    return result


inp = int(input())
count = 0
tmp_summ_list = []
string_values = {}
a = [i for i in range(inp**2) ]
random.shuffle(a)
matrix = [[ 0 for j in range(inp)] for i in range (inp)]
for i in range(inp):
    for j in range(inp):
        matrix[i][j] = a[count]
        count += 1
for i in matrix:
    print(i)
summm = sum_string(matrix)
for s in range(len(summm)):
    string_values[summm[s]] = matrix[s]
for i in string_values.keys():
    tmp_summ_list.append(i)
summ_list_sorted = sort(tmp_summ_list)
matrix_string_sorted = []
for i in summ_list_sorted:
    matrix_string_sorted.append(string_values[i])
matrix_string_sorted_tr = transpose(matrix_string_sorted)
sum_column = sum_string(matrix_string_sorted_tr)
column_values = {}
tmp_summ_col = []
for s in range(len(sum_column)):
    column_values[summm[s]] = matrix_string_sorted_tr[s]
for i in column_values.keys():
    tmp_summ_col.append(i)
summ_col_sorted = sort(tmp_summ_col)
matrix_col_sorted = []
for i in summ_col_sorted:
    matrix_col_sorted.append(column_values[i])
matrix_col_sorted_tr = transpose(matrix_col_sorted)
for i in matrix_col_sorted_tr:
    print(i)