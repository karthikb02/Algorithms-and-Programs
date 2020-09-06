def isValid(mat,row,col):
  for j in range(len(mat)):
    if mat[row][j]==1:
      return False
  for i in range(len(mat)):
    if mat[i][col]:
      return False
  row1=row
  col1=col
  while row1>=0 and col1>=0:
    if mat[row1][col1]==1:
      return False
    row1-=1
    col1-=1
  row2=row
  col2=col
  while row2>=0 and col2<N:
    if mat[row2][col2]==1:
      return False
    row2-=1
    col2+=1
  return True
def solveNqueen(matrix,row):
  if row>=len(matrix):
    return True
  for col in range(0,N):
    if(isValid(matrix,row,col)):
       matrix[row][col]=1
       if solveNqueen(matrix,row+1):
         return True
       matrix[row][col]=0
  return False
N=int(input())
matrix=[[0 for i in range(N)] for j in range(N)]
if solveNqueen(matrix,0)==False:
  print("Not Possible")
else:
  for i in matrix:
    print(*i)
          
      
       

