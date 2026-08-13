from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par= [i for i in range(len(edges)+1)]
        rank= [1]*(len(edges)+1)

        def find(n):
            p=par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def union(a,b):
            pa,pb= find(a),find(b)
            if pa==pb:
                return False
            
            if rank[pa]>rank[pb]:
                rank[pa]+=rank[pb]
                par[pb]=pa
            else:
                rank[pb]+=rank[pa]
                par[pa]=pb
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
            # print("P :",par)
            # print(" R: ",rank)

        return [0,0]