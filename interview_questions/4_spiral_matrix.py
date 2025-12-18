rows, cols = map(int,input("Enter rows and cols :").split())
matrix = [[0]*cols for i in range(rows)]

num = 1
top, left = 0, 0
bottom, right =  rows-1, cols-1

while top <= bottom and left <= right:

    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right,left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom,top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for i in matrix:
    print(i)
