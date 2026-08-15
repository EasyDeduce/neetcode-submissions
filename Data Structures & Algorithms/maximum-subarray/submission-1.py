class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        max_s=-1000000
        for i in nums:
            t=s+i
            s=max(0,s+i)
            if (t>max_s):
                max_s=t
        return max_s