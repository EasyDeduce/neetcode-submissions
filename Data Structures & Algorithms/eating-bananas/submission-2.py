class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        m=0
        for i in piles:
            m= max(m,i)
        l=1
        r=m
        while l<=r:
            mid= (l+r)//2
            tm=0
            for i in piles:
                tm-=(i//-mid)
            if tm>h:
                l=mid+1
            else:
                r=mid-1
        return l
        