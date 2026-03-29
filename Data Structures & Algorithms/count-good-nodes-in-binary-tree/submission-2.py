# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, max_node_so_far):
        if not root:
            return 0

        count = 0
        if root.val >= max_node_so_far:
            count = 1
            max_node_so_far = root.val

        count += self.dfs(root.right, max_node_so_far)
        count += self.dfs(root.left, max_node_so_far)

        return count
        