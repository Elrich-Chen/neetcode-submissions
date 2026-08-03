# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            res = ListNode(l1.val)
            l1 = l1.next
        else:
            res = ListNode(l2.val)
            l2 = l2.next

        start = res

        while l1 and l2:
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next

        if l1:
            res.next = l1
        elif l2:
            res.next = l2

        return start