from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ns= {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            ns[a].append(b)
        visitSet = set()    
        def dfs(crs):
            if crs in visitSet:
                return False
            if ns==[]:
                return True
            visitSet.add(crs)
            for value in ns[crs]:
                if not dfs(value): return False
            visitSet.remove(crs)
            ns[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


                    
            