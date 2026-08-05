class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr3 = dummy

        while list1 and list2:
            if list1.val < list2.val:
                ptr3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ptr3.next = ListNode(list2.val)
                list2 = list2.next

            ptr3 = ptr3.next

        while list1:
            ptr3.next = ListNode(list1.val)
            ptr3 = ptr3.next
            list1 = list1.next

        while list2:
            ptr3.next = ListNode(list2.val)
            ptr3 = ptr3.next
            list2 = list2.next

        return dummy.next