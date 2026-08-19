from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        myset=set()
        maxn=nums[0] if nums else None
        for i in range(len(nums)):
            if nums[i]<=0:
                continue
            maxn=max(maxn,nums[i])
            myset.add(nums[i])
        k= min(myset) if len(myset)>0 else None
        if k!=1:
            return 1
        while k:
            if k not in myset:
                return k
            k+=1
        return maxn+1