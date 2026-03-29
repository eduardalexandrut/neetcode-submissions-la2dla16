# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive(root:Optional[TreeNode], num):
    if root is None:
        return num
    l = recursive(root.left, num + 1)
    r = recursive(root.right, num + 1)
    return max(l,r)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return recursive(root, 0)
        
   