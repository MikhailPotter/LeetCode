# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            root = TreeNode(val=val)
            return root
        
        cur = root
        while cur:
            if cur.val < val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val=val)
                    return root
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val=val)
                    return root
        