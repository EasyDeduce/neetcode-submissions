class Solution:
    def dfs(self, grid:List[List[int]], i:int ,j:int)->int:
        if grid[i][j]==0:
            return 0
        grid[i][j]=0
        return 1+self.dfs(grid,min(len(grid)-1,i+1),j)+self.dfs(grid,i,min(len(grid[0])-1,j+1))+self.dfs(grid,max(0,i-1),j)+self.dfs(grid,i,max(0,j-1))


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_a=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    continue
                a= self.dfs(grid,i,j)
                if (a>max_a):
                    max_a=a
        return max_a