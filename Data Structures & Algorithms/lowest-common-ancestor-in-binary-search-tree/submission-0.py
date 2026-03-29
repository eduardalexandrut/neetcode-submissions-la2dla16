# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def isAncestor(root, p, q):
            if root is None:
                return None
            
            if root.val == p.val or root.val == q.val:
                return root
            else:
                l = isAncestor(root.left, p, q)
                r = isAncestor(root.right, p, q)

                if l and r:
                    return root
                
                return l if l else r
        return isAncestor(root, p, q)