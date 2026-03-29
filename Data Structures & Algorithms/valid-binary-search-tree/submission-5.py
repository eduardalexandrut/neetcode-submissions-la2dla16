# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inRange(-float('inf'), float('inf'), root)

        
    def inRange(self, low, high, root):
        if root is None:
            return True
        
        if not (low < root.val < high):
            return False
            
        return (self.inRange(low, root.val, root.left) and self.inRange(root.val, high, root.right))
        