class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def reverse(arr, start, end):
            for i in range(start,int((start+end)/2)):
                temp=arr[i]
                arr[i]= arr[end-1-(i-start)]
                arr[end-1-(i-start)]=temp
        
        reverse(nums,0,len(nums))
        reverse(nums,0,k)
        reverse(nums,k,len(nums))
        