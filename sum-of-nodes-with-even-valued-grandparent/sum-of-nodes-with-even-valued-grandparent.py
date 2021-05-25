# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.arr = []
        self.s = 0
        def traverse(root):
            if root is None:
                return
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        self.s += root.left.left.val
                    if root.left.right:
                        self.s += root.left.right.val
                if root.right:
                    if root.right.right:
                        self.s += root.right.right.val
                    if root.right.left:
                        self.s += root.right.left.val
            
                
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.s

       