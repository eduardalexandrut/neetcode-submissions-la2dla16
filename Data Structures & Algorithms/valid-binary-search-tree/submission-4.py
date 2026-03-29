# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, left, right):
            if root is None:
                return True

            #Current node val not in boundary
            if not (left < root.val < right):
                return False

            return isValid(root.left, left, root.val) and isValid(root.right, root.val, right)
    

        return isValid(root, float("-inf"), float("inf"))
