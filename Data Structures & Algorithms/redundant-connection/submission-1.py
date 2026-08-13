from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        def dfs(node,target,visited):
            if node==target:
                return True
            visited.add(node)
            for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    if dfs(neighbor,target,visited):
                        return True
            return False
        for u,v in edges:
            if dfs(u,v,set()):
                return [u,v]
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v,[]).append(u)
        return []