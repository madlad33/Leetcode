# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.is_true = False
        
        def has_path(root,target):
            if root is None:
                return
            target = target-root.val
            if target == 0 and not root.left and not root.right:
               print(root)
               self.is_true = True
            has_path(root.left,target)
            has_path(root.right,target)
        has_path(root,targetSum)
        return self.is_true