# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        def rec(cur_node, cur_sum):
        
            if not cur_node.right and not cur_node.left and cur_sum + cur_node.val == targetSum:
                return True

            cur_sum += cur_node.val

            r = False
            l = False
            if cur_node.right:
                r = rec(cur_node.right, cur_sum)
            if cur_node.left:
                l = rec(cur_node.left, cur_sum)
            
            return r or l

        return rec(root, 0)    
        