# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.s = 0
    
        def traverse(root,parent,grandparent):
            if root is None:
                return
            
            if grandparent is not None and grandparent.val % 2 == 0:
                self.s += root.val
                
            traverse(root.left,root,parent)
            traverse(root.right,root,parent)
        traverse(root,None,None)
        return self.s
       