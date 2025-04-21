# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        min_ = min(p.val, q.val)
        max_ = max(p.val, q.val)

        while root:
            if root.val > max_:
                root = root.left
            elif root.val < min_:
                root = root.right
            else: 
                return root
        return None
