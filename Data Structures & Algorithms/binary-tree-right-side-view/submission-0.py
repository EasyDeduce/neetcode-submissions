# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root:Optional[TreeNode])->List[int]:
        if not root:
            return []
        r= []
        q = deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                node  = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            x=level[-1]
            r.append(x)
        return r

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.levelOrder(root)
