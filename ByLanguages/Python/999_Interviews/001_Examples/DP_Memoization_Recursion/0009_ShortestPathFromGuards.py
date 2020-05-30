from collections import deque as queue

# get dimensions of the matrix - Select 5 as the value for now
Row = int(input("Enter Number Of Rows : "))
Column = int(input("Enter Number Of Columns : "))

def areMatrixSame(A,B):

   for i in range(Row):
      for j in range(Column):
         if (A[i][j] != B[i][j]):
            return False
   return True

# 4 neighbors of a given cell 
row = [-1, 0, 1, 0] 
col = [0, 1, 0, -1] 
  
# is in range 
def inRange(i, j): 
    if ((i < 0 or i > Row - 1) or (j < 0 or j > Column - 1)): 
        return False
    return True
  
# Have we visited the Cell 
def hasVisited(i, j,matrix, output): 
    if (matrix[i][j] != 'O' or output[i][j] != 'L'): 
        return False
    return True
  
# Function to replace all of the O's in the matrix 
# with their shortest distance from a guard 
def findDistance(matrix): 
    output = [[ -1 for i in range(Column)]for i in range(Row)] 
    q = queue() 
    # finding Guards location and adding into queue 
    for i in range(Row): 
        for j in range(Column): 
            # initialize each cell as L 
            output[i][j] = 'L'
            if (matrix[i][j] == 'G'): 
                pos = [i, j, 0] 
                q.appendleft(pos) 
                # guard 
                output[i][j] = 'G'
    # do till queue is empty 
    while (len(q) > 0): 
        # get the front cell in the queue and update 
        # its adjacent cells 
        curr = q.pop() 
        x, y, dist = curr[0], curr[1], curr[2] 
        # do for each adjacent cell 
        for i in range(4): 
            # if adjacent cell is valid, has path and 
            # not visited yet, en-queue it. 
            if inRange(x + row[i], y + col[i]) and hasVisited(x + row[i], y + col[i], matrix, output) : 
                output[x + row[i]][y + col[i]] = dist + 1
                pos = [x + row[i], y + col[i], dist + 1] 
                q.appendleft(pos) 
    # print matrix 
    for i in range(Row): 
        for j in range(Column): 
            #if output[i][j] > 0: 
            #    print(output[i][j], end=" ") 
            #else: 
            print(output[i][j],end=" ") 
        print()
    return output

#TestCase1  
matrix1 = [
			['G', 'O', 'O', 'O', 'O'], 
			['O', 'O', 'G', 'O', 'O'], 
			['O', 'O', 'O', 'O', 'O'], 
			['G', 'L', 'L', 'L', 'O'], 
			['O', 'O', 'O', 'O', 'G']
		] 

expectedResult1 = [
					['G', 1 , 1 , 2 , 3 ], 
					[ 1 , 1 ,'G', 1 , 2 ], 
					[ 1 , 2 , 1 , 2 , 2 ], 
					['G','L','L','L', 1 ], 
					[ 1 , 2 , 2 , 1 ,'G']
				  ] 

result1 = findDistance(matrix1) 

if (areMatrixSame(expectedResult1, result1)):
   print("Matrices are identical")
else:
   print("Matrices are not identical")

#TestCase2  
matrix2 = [
			['O', 'O', 'O', 'O', 'G'], 
			['O', 'L', 'L', 'O', 'O'], 
			['O', 'O', 'O', 'L', 'O'], 
			['G', 'L', 'L', 'L', 'O'], 
			['O', 'O', 'O', 'O', 'G']
		  ] 

expectedResult2 = [
					[ 3 , 3 , 2 , 1 ,'G'], 
					[ 2 ,'L','L', 2 , 1 ], 
					[ 1 , 2 , 3 ,'L', 2 ], 
					['G','L','L','L', 1 ], 
					[ 1 , 2 , 2 , 1 ,'G']
		] 

result2 = findDistance(matrix2) 

if (areMatrixSame(expectedResult2, result2)):
   print("Matrices are identical")
else:
   print("Matrices are not identical")

#TestCase3  
matrix3 = [
			['G','O','O','O','G'], 
			['O','L','O','L','O'], 
			['O','O','G','O','O'], 
			['O','L','O','L','O'], 
			['G','O','O','O','G']
		  ] 

expectedResult3 = [
					['G', 1 , 2 , 1 ,'G'], 
					[ 1 ,'L', 1 ,'L', 1 ], 
					[ 2 , 1 ,'G', 1 , 2 ], 
					[ 1 ,'L', 1 ,'L', 1 ], 
					['G', 1 , 2 , 1 ,'G']
		          ] 

result3 = findDistance(matrix3) 

if (areMatrixSame(expectedResult3, result3)):
   print("Matrices are identical")
else:
   print("Matrices are not identical")

# To Do - To Get A matrix from user and calculate distance on it
# To Do - To Work On Irregular Castle/Matrix