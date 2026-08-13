from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(1,len(edges)+1)]
        rank=[1]*len(edges)
        for u,v in edges:
            u=u-1
            v=v-1
            if (parent[u]==parent[v]):
                return [u+1,v+1]
            if rank[parent[u]-1]>=rank[parent[v]-1]:
                rank[parent[u]-1]=rank[parent[u]-1]+rank[parent[v]-1]
                t=parent[v]
                for i in range(len(parent)):
                    if parent[i]==t:
                        parent[i]=parent[u]
            else:
                rank[parent[v]-1]=rank[parent[v]-1]+rank[parent[u]-1]
                t=parent[u]
                for i in range(len(parent)):
                    if parent[i]==t:
                        parent[i]=parent[v]
            # print("P: ",parent)
            # print("R: ",rank)
        return [0,0]