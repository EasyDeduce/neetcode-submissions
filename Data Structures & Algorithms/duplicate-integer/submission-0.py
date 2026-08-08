class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset= set()
        for i in nums:
            if i in nset:
                return True
            else:
                nset.add(i)
        return False