class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for x in range(len(nums)):
            nums[x]=-nums[x]
        heapq.heapify(nums)
        self.h=nums

    def add(self, val: int) -> int:
        heapq.heappush(self.h, -val)
        tempq = self.h.copy()
        tempk = 1
        x= heapq.heappop(tempq)
        while tempq and tempk<self.k:
            x= heapq.heappop(tempq)
            tempk+=1
        return -x

