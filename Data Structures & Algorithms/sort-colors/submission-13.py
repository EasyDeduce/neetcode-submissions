class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l= 0
        r= len(nums)-1
        if nums[l]==2:
            t= nums[l]
            nums[l]=nums[r]
            nums[r]=t
            r-=1
        if  nums[r]==0:
            t= nums[l]
            nums[l]=nums[r]
            nums[r]=t
            l+=1
        for i in range(l,r+1):
            # print(i, nums[i], l, r , "          ", nums)
            if nums[l]==2 and l<r:
                t= nums[l]
                nums[l]=nums[r]
                nums[r]=t
                r-=1
            if  nums[r]==0 and l<r:
                t= nums[l]
                nums[l]=nums[r]
                nums[r]=t
                l+=1
            while i>=l and i<len(nums) and nums[i]==0:
                t= nums[l]
                nums[l]=nums[i]
                nums[i]=t
                l+=1
                i+=1
            while i>=0 and i<=r and nums[i]==2 :
                t= nums[r]
                nums[r]=nums[i]
                nums[i]=t
                r-=1
                i+=1