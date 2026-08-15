class Solution:
    def maxFrequency(self,nums:List[int],k:int)->int:
        t=set()
        initf= nums.count(k)
        for i in nums:
            t.add(i)
        mf=-1
        if k in t:
            t.remove(k)
            for i in t:
                f=initf
                for iter in range(len(nums)):
                    if nums[iter]==i:
                        f=f+1
                    elif nums[iter]==k:
                        f=max(initf,f-1)
                    if f>mf:
                        mf=f
        else:
            freq={}
            for i in nums:
                freq[i]=freq.get(i,0)+1
            mf= max(freq.values())
        return mf