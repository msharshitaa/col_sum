def col_sum(matrix,rows,cols):
    result=[]
    for i in range(rows):
        sum=0
        for j in range(cols):
            sum+=matrix[j][i]
        result.append(sum)
    return result
matrix=[]
rows=int(input("enter the no of rows:"))
cols=int(input("enter the no of cols:"))
for i in range(rows):
    matrix.append(list(map(int,input("enter elements:").split())))
print(col_sum(matrix,rows,cols))

