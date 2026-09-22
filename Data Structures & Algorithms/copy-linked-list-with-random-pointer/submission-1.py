"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {}
        def clone(node):
            if node is None:
                return None
            if node in copied:
                return copied[node]
            new_node = Node(node.val)
            copied[node] = new_node
            new_node.next = clone(node.next)
            new_node.random = clone(node.random)
            return new_node

        return clone(head)