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
        queue = deque([root])
        max_depth = 0

        while queue:
            for i in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.right:
                    queue.append(cur_node.right)
                if cur_node.left:
                    queue.append(cur_node.left)
            max_depth += 1
           
        return max_depth