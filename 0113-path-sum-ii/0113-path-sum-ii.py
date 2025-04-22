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

        def rec(cur_node, cur_path, cur_sum):
            nonlocal res

            cur_path.append(cur_node.val)
            cur_sum += cur_node.val

            if not cur_node.right and not cur_node.left:
                if cur_sum == targetSum:
                    return True, cur_path
                else:
                    return False, cur_path

            if cur_node.right:
                r, path = rec(cur_node.right, cur_path.copy(), cur_sum)
                if r:
                    res.append(path)
            if cur_node.left:
                l, path = rec(cur_node.left, cur_path.copy(), cur_sum)
                if l:
                    res.append(path)
            
            return False, cur_path
        
        b, path = rec(root, [], 0)
        if b: 
            res.append(path)
        return res            
