# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        node = head
        
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
        while l1:
            node.next = l1
            node = node.next
            l1 = l1.next
        while l2:
            node.next = l2
            node = node.next
            l2 = l2.next

        return head.next