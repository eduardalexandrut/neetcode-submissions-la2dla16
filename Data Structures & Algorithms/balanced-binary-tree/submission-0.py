# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recursive(root:Optional[TreeNode]):
    if root is None:
        return True, 0
    l_bal,l_height = recursive(root.left)
    r_bal, r_height = recursive(root.right)
    is_balanced =  (abs(l_height-r_height)) <= 1 and l_bal and r_bal
    height = max(l_height, r_height) + 1
    return is_balanced, height
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return recursive(root)[0]
        
