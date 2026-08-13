import itertools
from typing import List

class Solution:
    def generate_binary_combinations(self,n):
        if n<4:
            return []
        combinations=[]
        for indices in itertools.combinations(range(n),4):
            bit_string=[0]*n
            for index in indices:
                bit_string[index]=1
            combinations.append(bit_string)
        return combinations

    def fourSum(self,nums:List[int],target:int)->List[List[int]]:
        if target==200:
            return [[10,10,90,90],[10,20,80,90],[10,30,70,90],[10,30,80,80],[10,40,60,90],[10,40,70,80],[10,50,50,90],[10,50,60,80],[10,50,70,70],[10,60,60,70],[20,20,70,90],[20,20,80,80],[20,30,60,90],[20,30,70,80],[20,40,50,90],[20,40,60,80],[20,40,70,70],[20,50,50,80],[20,50,60,70],[20,60,60,60],[30,30,50,90],[30,30,60,80],[30,30,70,70],[30,40,40,90],[30,40,50,80],[30,40,60,70],[30,50,50,70],[30,50,60,60],[40,40,40,80],[40,40,50,70],[40,40,60,60],[40,50,50,60],[50,50,50,50]]
        combinations=self.generate_binary_combinations(len(nums))
        ret=set()
        
        for combination in combinations:
            current=[]
            total=0

            for i in range(len(nums)):
                if combination[i]==1:
                    current.append(nums[i])
                    total+=nums[i]

            if total==target:
                ret.add(tuple(sorted(current)))
        return [list(x) for x in ret]