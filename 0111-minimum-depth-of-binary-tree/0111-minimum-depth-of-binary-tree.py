# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        min_depth = 0
        tree_end = False

        while queue:
            for i in range(len(queue)):
                cur_node = queue.popleft()
                if not cur_node.left and not cur_node.right:
                   tree_end = True
                if cur_node.right:
                    queue.append(cur_node.right)
                if cur_node.left:
                    queue.append(cur_node.left)
            min_depth += 1
            if tree_end:
                return min_depth

            


        