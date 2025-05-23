# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return False

        values_set = set()
        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if cur.val in values_set:
                return True
            diff = k - cur.val
            values_set.add(diff)
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
        return False

        