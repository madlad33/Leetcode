# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        dummy = TreeNode()
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        
        dummy_root = curr = TreeNode(val=self.arr[0])
        for i in range(1,len(self.arr)):
            dummy_root.right = TreeNode(val=self.arr[i])
            dummy_root = dummy_root.right
        return curr
            
            
            
            