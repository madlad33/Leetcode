# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #[0,1,2,3,4,5,6,7,8]
        self.val = 0
        def inorder(root):
            if root is None:
                return 0
            right = inorder(root.right)
            self.val += root.val
            root.val = self.val
            left = inorder(root.left)
         
        inorder(root)
        return root
        