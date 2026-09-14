class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dmap= {}
        for i in range(len(nums)):
            if nums[i] in dmap:
                if abs(i-dmap.get(nums[i]))<=k:
                    return True
            dmap[nums[i]]=i
        return False