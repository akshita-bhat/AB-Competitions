mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
mat_sum_forward = 0
mat_sum_backward = 0
row = len(mat)
col = row 

# forward diagnol 
for i in range(row):
    mat_sum_forward+=mat[i][i]

# backword diagnol 
for i in range(row):
    mat_sum_backward+=mat[i][row-i-1]

# final sum
if row%2!=0:
    print(mat_sum_forward+mat_sum_backward-mat[int((row-1)/2)][int((row-1)/2)])
else:
    print(mat_sum_forward, mat_sum_backward)        

