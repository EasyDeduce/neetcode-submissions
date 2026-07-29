class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #min stack using doule ended queue
        output=[]
        q= collections.deque()
        l=r=0
        while (r<len(nums)):
            #pop smaller values from q
            while q and nums[q[-1]]<=nums[r]:
                q.pop()
            q.append(r)
            while l>q[0]:
                q.popleft()
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output


            


            
                        
            