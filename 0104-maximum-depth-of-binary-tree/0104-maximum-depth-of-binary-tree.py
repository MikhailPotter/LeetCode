# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def rec(cur_node):
            r, l = 0, 0
            if cur_node.right:
                r = rec(cur_node.right)
            if cur_node.left:
                l = rec(cur_node.left)
            return max(r+1, l+1)
            
        res = rec(root)  
        return res