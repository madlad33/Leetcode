# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.arr_1 = []
        self.arr_2 = []
        
        def get_leaves_tree_1(root):
            if root is None:
                return 
            if root.left is None and root.right is None:
                self.arr_1.append(root.val)
            get_leaves_tree_1(root.left)
            get_leaves_tree_1(root.right)
        
        get_leaves_tree_1(root1)
        self.arr_2 = self.arr_1
        self.arr_1 = []
        get_leaves_tree_1(root2)
        if self.arr_1 == self.arr_2:
            return True
        return False