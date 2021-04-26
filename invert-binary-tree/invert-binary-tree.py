# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def mirror(root):
            if root is None:
                return
            mirror(root.left)
            mirror(root.right)
            
            root.left,root.right = root.right, root.left
            return root
        return mirror(root)
        
        
        
        
       