# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None:
            if q == None:
                return True
            return False
        elif q == None:
            return False

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            for i in range(len(queue1)):

                cur_node1 = queue1.popleft()
                cur_node2 = queue2.popleft()

                if cur_node1.val != cur_node2.val:
                    return False

                if cur_node1.right:
                    if cur_node2.right:
                        queue1.append(cur_node1.right)
                        queue2.append(cur_node2.right)
                    else:
                        return False
                elif cur_node2.right:
                    return False
                
                if cur_node1.left:
                    if cur_node2.left:
                        queue1.append(cur_node1.left)
                        queue2.append(cur_node2.left)
                    else:
                        return False
                elif cur_node2.left:
                    return False

        if not queue1 and not queue2:     
            return True
        return False
        