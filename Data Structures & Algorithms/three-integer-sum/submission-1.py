class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,tri=[],[]

        def kSum(k,start,target):
            if k>2:
                for i in range(start, len(nums)-k+1):
                    if start<i and nums[i]==nums[i-1]:
                        continue
                    tri.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    tri.pop()
                return 
            l=start
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    res.append(tri+[nums[l],nums[r]])
                    l+=1
                    while l<r and (nums[l]==nums[l-1]):
                        l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
        
        kSum(3,0,0)
        return res