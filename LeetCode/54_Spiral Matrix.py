def spiralOrder(matrix) :
        res = []
        top , left = 0, 0
        bottom, right = len(matrix), len(matrix[0])
        m = len(matrix)
        n = len(matrix[0])
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(right,bottom):
                 res.append(matrix[right][i])
            
        return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(mat))