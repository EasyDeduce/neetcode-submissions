class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fmap={}
        for i in range(len(nums)):
            fmap[nums[i]]= fmap.get(nums[i],0)+1
        return max(fmap,key=fmap.get)