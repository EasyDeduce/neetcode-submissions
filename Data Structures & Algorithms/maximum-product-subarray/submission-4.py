class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max=1
        curr_min=1
        for i in range(len(nums)):
            temp = curr_max * nums[i]
            curr_max = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_min = min(temp, nums[i] , nums[i]*curr_min)
            res = max(res, curr_max)
        return res