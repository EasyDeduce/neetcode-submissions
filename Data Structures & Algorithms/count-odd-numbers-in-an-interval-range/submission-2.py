class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low==high and low%2==0:
            return 0
        if low==high and low%2!=0:
            return 1
        return ((high-low)//2+1)