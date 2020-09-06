S1=input().strip()
S2=input().strip()
C=len(S1)
R=len(S2)
matrix=[[0 for col in range(C+1)] for row in range(R+1)]
for col in range(C+1):
    matrix[0][col]=col
for row in range(R+1):
    matrix[row][0]=row
for row in range(1,R+1):
    for col in range(1,C+1):
        if S2[row-1]==S1[col-1]:
            matrix[row][col]=matrix[row-1][col-1]
        else:
            matrix[row][col]=min(matrix[row-1][col],matrix[row][col-1],mat[row-1][col-1])+1
for row in matrix:
    print(*row)
print(matrix[R][C])
