# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None or p == root or q == root: 
            return root
        
        if p.val > root.val or q.val > root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        else:
            right = None
        if p.val < root.val or q.val < root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
        else:
            left = None

        if left != None and right != None:
            return root
        if left != None:
            return left
        return right