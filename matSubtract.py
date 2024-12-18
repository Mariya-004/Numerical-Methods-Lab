def matSub(mat_1, mat_2, r, c):
    mat=[]
    for i in range(r):
        row=[]
        for j in range(c):
            dif=mat_1[i][j]-mat_2[i][j]
            row.append(dif)
        mat.append(row)
    return mat
n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
print("First matrix")
mat1=[]
for i in range(n):
    rows=[]
    for j in range(m):
        a=int(input("Enter the element:"))
        rows.append(a)
    mat1.append(rows)
print(mat1)
print("---------------------------------------------------")
print("Second matrix")
mat2=[]
for i in range(n):
    rows=[]
    for j in range(m):
        a=int(input("Enter the element:"))
        rows.append(a)
    mat2.append(rows)
print(mat2)
print("Difference of the matrices is")
mat=matSub(mat1, mat2, n, m)
print(mat)
