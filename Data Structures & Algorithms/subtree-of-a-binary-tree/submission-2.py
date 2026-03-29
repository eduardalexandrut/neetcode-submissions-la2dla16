class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. If the main tree is empty, subRoot can't be in it
        if not root: 
            return False
        
        # 2. If the trees are identical starting here, we found it!
        if self.isSameTree(root, subRoot):
            return True
        
        # 3. Otherwise, search in the left and right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty? They are the same.
        if not p and not q:
            return True
        # One empty or values don't match? Not the same.
        if not p or not q or p.val != q.val:
            return False
        
        # Check if left subtrees match AND right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)