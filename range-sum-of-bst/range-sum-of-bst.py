# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum_ = 0
        def rangesum(root,low,high):
            if root is None:
                return
            if low<=root.val<=high:
                self.sum_+=root.val
            rangesum(root.left,low,high)
            rangesum(root.right,low,high)
        rangesum(root,low,high)
        return self.sum_
    
            