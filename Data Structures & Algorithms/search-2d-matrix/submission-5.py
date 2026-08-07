class Solution:
    def b_search_rows(self, matrix: List[List[int]],target: int, start: int, end: int)-> int:
        if start<end:
            if matrix[start][0]==target:
                print(1," ")
                return start
            if matrix[end][0]==target:
                print(12," ")
                return end
            mid= int((start+end)/2)
            if matrix[mid][0]==target:
                print(123," ")
                return mid
            elif matrix[mid][0]>target:
                print(1234," ")
                return self.b_search_rows(matrix, target, start, mid)
            else:
                print(12345," ")
                return self.b_search_rows(matrix, target, mid+1, end)
        elif start==end:
            if matrix[start][0]==target:
                return start
            elif matrix[start][0]>target:
                return start-1
            else:
                return start
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=self.b_search_rows(matrix, target,0,len(matrix)-1)
        print(i)
        for j in range(len(matrix[0])):
            if (matrix[i][j]==target):
                return True
            elif (matrix[i][j]>target):
                return False
        return False
