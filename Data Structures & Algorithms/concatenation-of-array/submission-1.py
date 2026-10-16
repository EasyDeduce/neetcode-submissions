class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp= [0]*(2*len(nums))
        for i,num in enumerate(nums):
            temp[i]=num
            temp[i+len(nums)]=temp[i]
        return temp