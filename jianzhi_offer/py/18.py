# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        return head