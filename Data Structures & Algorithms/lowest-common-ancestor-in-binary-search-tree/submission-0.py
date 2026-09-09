# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l=min(p.val,q.val)
        h=max(p.val,q.val)
        
        def dfs(t: TreeNode):
            if t==None:
                return False
            if t.val== p.val or t.val==q.val:
                return True
            return dfs(t.left) and dfs(t.right)
        temp=root
        while temp!=None:
            if temp.val>=l and temp.val<=h:
                if dfs(temp):
                    res=temp.val
                return temp
            elif h<temp.val:
                temp= temp.left
            elif l>temp.val:
                temp= temp.right
        