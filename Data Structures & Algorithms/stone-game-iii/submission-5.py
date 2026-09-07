class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        cache={}
        def dfs(i):
            if i==len(values):
                return 0
            if i in cache:
                return cache[i]
            res= float("-inf")
            for j in range(i,min(i+3,len(values))):
                res= max(res,sum(values[i:j+1])-dfs(j+1))
            cache[i]= res
            return res

        x= dfs(0)
        if x==0:
            return "Tie"
        elif x>0:
            return "Alice"
        else:
            return "Bob"
        