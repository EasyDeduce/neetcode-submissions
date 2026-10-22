class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []
        nums.sort()
        def backtrack(idx):
            if idx>=len(nums):
                ret.append(temp.copy())
                return
            
            temp.append(nums[idx])
            backtrack(idx+1)
            temp.pop()
            a= nums[idx]
            while idx<len(nums) and nums[idx]==a:
                idx+=1
            backtrack(idx)

        backtrack(0)
        return ret
            

