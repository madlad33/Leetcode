# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.r = None
        def traverse(root,target):
            if root is None:
                return
            if root.val == target.val:
                self.r = root
                
            traverse(root.left,target)
            traverse(root.right,target)
        traverse(cloned,target)
        return self.r