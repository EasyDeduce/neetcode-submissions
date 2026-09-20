class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:  
        l=[]
        temp=[]
        cache=set()
        def dfs(i,s):
            if s==target:
                if set(temp.copy()) not in cache:
                    l.append(temp.copy())
                return
            elif s>target:
                return  
            for j in range(i,len(nums)):
                temp.append(nums[j])
                s+=nums[j]
                dfs(j,s)
                s-=nums[j]
                temp.pop()
        dfs(0,0)
        return l
