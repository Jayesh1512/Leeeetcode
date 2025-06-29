# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(root, cmax):
            if root is None:
                return 0 

            left = rec(root.left, cmax)
            right = rec(root.right, cmax)
            cmax[0] = max(cmax[0], left + right)

            return max(left, right) + 1 

        cmax = [0]
        rec(root, cmax)
        return cmax[0]
