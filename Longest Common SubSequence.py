S1=input().strip()
S2=input().strip()
R=len(S1)
C=len(S2)
matrix=[[0 for col in range(C+1)] for row in range(R+1)]
for row in range(R+1):
  for col in range(C+1):
    if row==0 or col==0:
      matrix[row][col]=0
    elif S1[row-1]==S2[col-1]:
      matrix[row][col]=matrix[row-1][col-1]+1
    else:
      matrix[row][col]=max(matrix[row][col-1],matrix[row-1][col])
print(matrix[R][C])  
