# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return root
        stack = [root]

        while stack:
            cur_node = stack.pop()
            if cur_node:
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                stack.extend([cur_node.left, cur_node.right])
        return root
            

        