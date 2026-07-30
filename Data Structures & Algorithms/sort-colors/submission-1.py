class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if (nums[i]>nums[j]):
                    t= nums[j]
                    nums[j]=nums[i]
                    nums[i]=t
              