# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        v = set()
        temp = headA
        while(temp != None):
            v.add(temp)
            temp = temp.next
        t2 = headB
        while(t2 != None):
            if t2 in v:
                return t2
            t2 = t2.next
        return None
        