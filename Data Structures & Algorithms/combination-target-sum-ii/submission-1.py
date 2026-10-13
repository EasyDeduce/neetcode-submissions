class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            soln=[]
            temp=[]
            candidates.sort()
            s=0
            def dfs(idx, s):
                if s==target:
                    soln.append(temp.copy())
                    return
                elif s>target:
                    return
                for j in range(idx,len(candidates)):
                    if j>idx and candidates[j]==candidates[j-1]:
                        continue
                    temp.append(candidates[j])
                    s+=candidates[j]
                    dfs(j+1,s)
                    s-=candidates[j]
                    temp.pop()
            dfs(0,0)
            return soln

