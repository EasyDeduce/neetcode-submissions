class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        
        def dfs(i):
            if i>=len(nums):
                # since python is dynamically typed, subset will always be modified, so we add a static copy of it instead of adding it directly
                res.append(subset.copy())
                return 
            #include the ith index number
            subset.append(nums[i])
            dfs(i+1)
            #don't include the ith index number
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res