# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#class Solution:
#    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#        arr = []
#        def dfs(root, arr):
#            if root is None:
#                return
#            arr.append(root.val)
#            dfs(root.left, arr)
#            dfs(root.right, arr)

#        dfs(root, arr)
#        arr.sort()
#       return arr[k-1]
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right
