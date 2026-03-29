from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        results = []
        queue = deque([root])  # Start with the root in the queue
        
        while queue:
            level_size = len(queue)  # How many nodes are on the current level
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()  # Get the next node in line
                current_level.append(node.val)
                
                # Add children to the queue for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            results.append(current_level)
            
        return results