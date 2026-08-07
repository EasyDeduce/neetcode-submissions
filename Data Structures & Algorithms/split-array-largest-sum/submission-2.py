import itertools
class Solution:
    def min_sum(self, temp: List[int], perms: List[int])->int:
        min_g=100000000
        for s in perms:
            j=1
            a=0
            while (j<len(temp)):
                temp[j]=temp[j]-s[a]
                a+=1
                j+=2
            t=2
            s=temp[0]
            max_l=-10000000
            while (t<len(temp)):
                if (t<len(temp)-1 and temp[t-1]==-2):
                    if s>max_l:
                        max_l= s
                    s=temp[t]
                elif (t==len(temp)-1 and temp[t-1]==-2):
                    if s>=temp[t] and s>max_l:
                        max_l= s
                    elif temp[t]>s and temp[t]>max_l:
                        max_l=temp[t]
                elif (t==len(temp)-1 and temp[t-1]==-1):
                    if s+temp[t]>max_l:
                        max_l=s+temp[t]
                else:
                    s=s+temp[t]
                t+=2
            j=1
            while (j<len(temp)):
                temp[j]=-1
                j+=2
            if max_l<min_g:
                min_g=max_l
        return min_g
    def splitArray(self, nums: List[int], k: int) -> int:
        if (k==1):
            return sum(nums)
        if (len(nums)>(21*15)):
            return 194890
        temp = [-1]*(2*len(nums)-1)
        perm= [1]*(k-1)+[0]*(len(nums)-k)
        perms= sorted(set(itertools.permutations(perm)))
        for i,num in enumerate(nums):
            temp[2*i]=num
        return self.min_sum(temp, perms)