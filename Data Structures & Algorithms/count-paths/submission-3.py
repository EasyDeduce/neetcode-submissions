class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        graph=[[0 for _ in range(m)] for _ in range(n)]
        graph[n-1][m-1]=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i+1>n-1:
                    graph[i][j]= graph[i][min(m-1,j+1)]
                elif j+1>m-1:
                    graph[i][j]= graph[min(n-1,i+1)][j]
                else:
                    graph[i][j]= graph[i][min(m-1,j+1)]+ graph[min(n-1,i+1)][j]
            # print(graph[i])
            
        return graph[0][0]