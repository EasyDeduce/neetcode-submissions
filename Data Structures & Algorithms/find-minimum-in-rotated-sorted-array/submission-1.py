class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        else:
            i=0
            while nums[i]>nums[len(nums)-1-i]:
                i+=1
            return min(nums[i],nums[min(len(nums)-1,len(nums)-i)])