class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        for i in range(len(matrix)):
            if(matrix[i][0]==target):
                return True
            elif (matrix[i][0]>target):
                i=i-1
                break
        print(i)
        for j in range(len(matrix[0])):
            if (matrix[i][j]==target):
                return True
            elif (matrix[i][j]>target):
                return False
        return False
