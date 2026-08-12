class Solution:
    def dfs(self, visited:List[List[int]], grid:List[List[int]], i:int ,j:int)->int:
        if (visited[i][j]==1):
            return 0
        else:
            visited[i][j]=1
            if grid[i][j]==0:
                return 0
            return grid[i][j]+self.dfs(visited,grid,min(len(grid)-1,i+1),j)+self.dfs(visited,grid,i,min(len(grid[0])-1,j+1))+self.dfs(visited,grid,max(0,i-1),j)+self.dfs(visited,grid,i,max(0,j-1))


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_a=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a= self.dfs(visited,grid,i,j)
                if (a>max_a):
                    max_a=a
        return max_a