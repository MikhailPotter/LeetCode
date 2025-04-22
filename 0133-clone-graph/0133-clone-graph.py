"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone_graph = {}
        queue = deque([node])
        clone_graph[node] = Node(node.val)

        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in clone_graph:
                    clone_graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_graph[cur_node].neighbors.append(clone_graph[neighbor])
        
        return clone_graph[node]


            
        