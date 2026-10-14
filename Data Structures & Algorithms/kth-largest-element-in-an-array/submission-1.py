class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        n=0
        while k>0:
            n= heapq.heappop(nums)
            k-=1
        return -n