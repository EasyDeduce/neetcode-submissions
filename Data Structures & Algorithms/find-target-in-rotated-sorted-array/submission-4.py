class Solution:
    def binary(self, nums:List[int], target:int, start:int, end:int, rot:int)->int:
        # print(start,nums[start], rot,end, nums[end],target)
        # print(start,end)
        s_t= max((len(nums)+start-rot)%len(nums), start-rot)
        e_t= max((len(nums)+end-rot)%len(nums), end-rot)
        # print(s_t,e_t)
        if (s_t==e_t):
            if (nums[start]==target):
                return start
            else:
                return -1
        
        if (nums[start]==target):
            return start
        if (nums[end]==target):
            return end
        
        mid_t= int((s_t+e_t)/2)
        mid= (mid_t+rot)%len(nums)
        # print(mid,mid_t,len(nums))
        if (nums[mid]==target):
            return mid
        elif (nums[mid]<target):
            return self.binary(nums,target, (mid+1)%len(nums), end, rot)
        else:
            return self.binary(nums, target, start, mid, rot)

    def search(self, nums: List[int], target: int) -> int:
        # print(target)
        if (nums[0]<nums[-1]):
            return self.binary(nums,target,0,len(nums)-1,0)
        j=0
        if(len(nums)==1):
            if nums[0]==target: return 0
            else: return -1
        while (nums[j]<nums[j+1]):
            j+=1
        return self.binary(nums,target,j+1,j,j+1)