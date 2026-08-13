class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapf={}
        for i,n in enumerate(nums):
            if target-n in mapf:
                return [mapf[target-n],i]
            mapf[n]=i
        
