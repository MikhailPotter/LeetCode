# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diam = 0

        def depth(cur_node):
            nonlocal max_diam
            r = depth(cur_node.right) if cur_node.right else 0
            l = depth(cur_node.left) if cur_node.left else 0

            max_diam = max(max_diam, r + l) 

            return max(r, l) + 1
        
        depth(root)
        return max_diam
   