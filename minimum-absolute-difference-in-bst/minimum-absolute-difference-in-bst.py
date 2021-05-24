# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_d = float('inf')
        self.arr = []
        def min_dist(root):
            if root is None:
                return
            min_dist(root.left)
            self.arr.append(root.val)
            min_dist(root.right)
        min_dist(root)
        
        for i in range(len(self.arr)-1):
            diff = abs(self.arr[i] - self.arr[i+1])
            self.min_d = min(self.min_d,diff)
        return self.min_d
            
            #             if root is None:
#                 return 
#             if not root.left and not root.right:
#                 return
#             left_val,right_val = float('inf'),float('inf')
#             if root.left:
#                 left_val = abs(root.val - root.left.val)
#             if root.right:
#                 right_val = abs(root.val - root.right.val)

#             self.min_d = min(self.min_d,left_val,right_val)
#             min_dist(root.left)
#             min_dist(root.right)
#         min_dist(root)
#         return self.min_d