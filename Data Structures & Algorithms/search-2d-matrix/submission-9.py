class Solution:
    def b_search_rows(self, matrix: List[List[int]],target: int, start: int, end: int)-> int:
        if start<end:
            if matrix[start][0]==target:
                return start
            if matrix[end][0]==target:
                return end
            mid= int((start+end)/2)
            if matrix[mid][0]==target:
                return mid
            elif matrix[mid][0]>target:
                return self.b_search_rows(matrix, target, start, mid)
            else:
                return self.b_search_rows(matrix, target, mid+1, end)
        elif start==end:
            if matrix[start][0]==target:
                return start
            elif matrix[start][0]>target:
                return start-1
            else:
                return start
    def b_search_columns(self, matrix: List[List[int]], i :int, start:int, end:int, target:int)->int:
        if start<end:
            if matrix[i][start]==target:
                return start
            if matrix[i][end]==target:
                return end
            mid= int((start+end)/2)
            if matrix[i][mid]==target:
                return mid
            elif matrix[i][mid]>target:
                return self.b_search_columns(matrix, i,start, mid-1,target)
            else:
                return self.b_search_columns(matrix, i,mid+1, end, target)
        elif start==end:
            if matrix[i][start]==target:
                return start
            else:
                return -1 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=self.b_search_rows(matrix, target,0,len(matrix)-1)
        j= self.b_search_columns(matrix, i, 0,len(matrix[0])-1, target)
        if (j==-1 or j==None):
            return False
        return True
