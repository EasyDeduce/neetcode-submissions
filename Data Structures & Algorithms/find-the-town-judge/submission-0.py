class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        matrix= [[0 for _ in range(n)] for _ in range(n)]
        for i,j in trust:
            matrix[i-1][j-1]=1
        judge=-1
        print(matrix)
        for i in range(len(matrix[0])):
            t=0
            for j in range(len(matrix)):
                if (i!=j and matrix[j][i]):
                    t+=1
            if (t==n-1):
                k=i
                x=0
                for m in range(len(matrix[0])):
                    if (matrix[k][m]!=0):
                        x=1
                        break
                if (x==0): judge=i+1 
        return judge                                  