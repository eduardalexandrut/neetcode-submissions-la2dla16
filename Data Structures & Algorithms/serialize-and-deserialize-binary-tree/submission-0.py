# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"
        
        preS = []
        inS = []

        def inorder(root, inS):
            if root is None:
                return
            inorder(root.left, inS)
            inS.append(str(root.val))
            inorder(root.right, inS)

        def preorder(root, preS):
            if root is None:
                return
            preS.append(str(root.val))
            preorder(root.left, preS)
            preorder(root.right, preS)

        inorder(root, inS)
        preorder(root, preS)
        
        # Join inorder and preorder lists with commas
        inS = ','.join(inS)
        preS = ','.join(preS)
        
        # Return the combined string
        res = inS + "#" + preS
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "#":
            return None

        inorder_s = data.split('#')[0]
        preorder_s = data.split('#')[1]
        
        # If either string is empty, handle that case
        if not inorder_s or not preorder_s:
            return None
        
        # Convert strings to integer lists
        inorder = [int(x) for x in inorder_s.split(',') if x]
        preorder = [int(x) for x in preorder_s.split(',') if x]
        
        # Helper function to build the tree
        def buildTree(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            # Root node is the first element in preorder
            root = TreeNode(preorder[0])
            
            # Find the index of the root in inorder list
            mid = inorder.index(preorder[0])
            
            # Recursively build the left and right subtrees
            root.left = buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
            
            return root
        
        return buildTree(preorder, inorder)
