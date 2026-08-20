# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while (fast!=None):
            slow=slow.next
            fast=fast.next.next
        t=head
        broken=t.next
        t.next= None
        while broken!=None and broken!=slow:
            temp=broken
            broken=broken.next
            temp.next=t
            t=temp
        ms=-1
        print(t.val,slow.val)
        while t!=None and slow!=None:
            ms=max(t.val+slow.val,ms)
            t=t.next
            slow=slow.next
        return ms