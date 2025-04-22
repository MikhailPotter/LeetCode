# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []

        res = list()

        def rec(cur_node, path, cur_sum):
            path.append(cur_node.val)
            cur_sum += cur_node.val

            if not cur_node.right and not cur_node.left:
                if cur_sum == targetSum:
                    res.append(list(path))
                path.pop() 
                return

            if cur_node.right:
                rec(cur_node.right, path, cur_sum)
            if cur_node.left:
                rec(cur_node.left, path, cur_sum)

            path.pop()

        rec(root, [], 0)
        return res            
