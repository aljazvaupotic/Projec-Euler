#spiralni 2d array 1001x1001 start v sredini 
size = 1001
rows = size
colums = size
leftSum = 0
rightSum = 0
row = 0
colum = size-1
i = size*size
spiral = [[0 for i in range(colums)] for j in range(rows)]
while i > 0:

    #print(row,colum)
    while colum >= 0 and spiral[row][colum] == 0:
        spiral[row][colum] = i
       # print(spiral[row][colum])

        i -= 1
        colum -= 1
    colum += 1
    row += 1

   # print(row,colum)
    while row < rows and spiral[row][colum] == 0:
        spiral[row][colum] = i
        #print(spiral[row][colum])
        i -= 1
        row += 1
    row -= 1
    colum += 1

    while colum < colums and spiral[row][colum] == 0:
        spiral[row][colum] = i
        #print(spiral[row][colum])
        i -= 1
        colum += 1
    colum -= 1
    row -= 1

    while row >= 0 and spiral[row][colum] == 0:
        spiral[row][colum] = i
        #print(spiral[row][colum])
        i -= 1
        row -= 1
    row += 1
    colum -=1

for x in range(0,size):
    leftSum += spiral[x][x]
    rightSum += spiral[size-1-x][x]

print(leftSum + rightSum - 1)