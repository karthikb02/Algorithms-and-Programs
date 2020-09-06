def isValid(matrix,row,col,val):
  for ctr in range(9):
    if matrix[row][ctr]==val or matrix[ctr][col]==val:
      return False
  sRow=row-row%3
  sCol=col-col%3
  for i in range(sRow,sRow+3):
    for j in range(sCol,sCol+3):
      if matrix[i][j]==val:
        return False
  return True

def solveSuduko(matrix,row,col):
  if col>=9:
    row+=1
    col=0
  if row>=9:
    return True
  if matrix[row][col]!=0:
    if solveSuduko(matrix,row,col+1):
      return True
  else:
    for val in range(1,10):
      if isValid(matrix,row,col,val):
        matrix[row][col]=val
        if solveSuduko(matrix,row,col+1):
          return matrix
        matrix[row][col]=0
  return False
sudukoMatrix=[list(map(int,input().split())) for i in range(9)]
if not solveSuduko(sudukoMatrix,0,0):
  print("NOT Valid")
else:
  for rows in sudukoMatrix:
    print(*rows)
