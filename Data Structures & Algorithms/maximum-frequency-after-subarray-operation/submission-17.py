class Solution:
    def maxFrequency(self,nums:List[int],k:int)->int:
        initf= nums.count(k)
        if initf==0:
            freq={}
            for i in nums:
                freq[i]=freq.get(i,0)+1
            return max(freq.values())

        t=set()
        for i in nums:
            if i not in t and i!=k:
                t.add(i)
        mf=-1
        for i in t:
            f=initf
            for iter in range(len(nums)):
                if nums[iter]==i:
                    f=f+1
                elif nums[iter]==k:
                    f=max(initf,f-1)
                mf=max(mf,f)
        return mf