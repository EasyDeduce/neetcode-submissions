# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def binary_search(self, start, end):
        mid = int((start+end)/2)
        res = guess(mid)
        if res==0:
            return mid
        elif res==-1:
            return self.binary_search(start,mid-1)
        else:
            return self.binary_search(mid+1,end)
        
    def guessNumber(self, n: int) -> int:
        return self.binary_search(0,n)