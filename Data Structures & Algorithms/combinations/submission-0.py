class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        temp=[]
        cache={}
        def dfs(idx, k):
            if k==0:
                ret.append(temp.copy())
                return
            if k>(n-idx+1):
                return 
            for i in range(idx, n+1):
                temp.append(i)
                dfs(i+1, k-1)
                temp.pop()
        dfs(1,k)
        return ret