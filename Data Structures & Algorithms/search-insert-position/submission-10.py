class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            if l==r and target==nums[l]:
                return l
            if target>nums[l]:
                l+=1
            if target<nums[r]:
                r-=1
        # print(r,l)
        return max(r,l)