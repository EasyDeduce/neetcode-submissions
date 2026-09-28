class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x= -heapq.heappop(stones)
            y= -heapq.heappop(stones)
            if x==y:
                continue
            elif x>y:
                heapq.heappush(stones, -(x-y))
            else:
                heapq.heappush(stones, -(y-x))
        if len(stones)==0:
            return 0
        return -stones[-1]