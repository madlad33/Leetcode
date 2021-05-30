# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count_good(root,max_val):
            if root is None:
                return 0
            else:
                is_good = root.val >= max_val
                left = count_good(root.left,max(max_val,root.val))
                right = count_good(root.right,max(max_val,root.val))
                return left + right + is_good
        return count_good(root,float('-inf'))