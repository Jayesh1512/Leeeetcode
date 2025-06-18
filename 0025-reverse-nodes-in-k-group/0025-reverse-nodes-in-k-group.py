# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def rev(prev, head, k):
            i = 0
            curr = head 
            while curr is not None and i < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1
            return prev, curr 

        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        total_nodes = count_nodes(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        while total_nodes >= k:
            tail = curr
            new_head, next_group_start = rev(None, curr, k)
            prev_group_end.next = new_head
            tail.next = next_group_start
            prev_group_end = tail
            curr = next_group_start
            total_nodes -= k

        return dummy.next
