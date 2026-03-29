"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_to_new = {}
        
        def bfs(node):
            q = deque([node])
            old_to_new[node] = Node(node.val)

            
            while q:
                temp = q.popleft()
    
                for n in temp.neighbors:
                    if n not in old_to_new:
                       old_to_new[n] = Node(n.val)
                       q.append(n)
                    old_to_new[temp].neighbors.append(old_to_new[n])
        
        bfs(node)
        return old_to_new[node]



        