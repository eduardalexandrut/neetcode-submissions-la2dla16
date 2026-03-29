# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recursive(root: Optional[TreeNode]):
    if root is None:
        return
    recursive(root.left)
    recursive(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        recursive(root)
        return root
        