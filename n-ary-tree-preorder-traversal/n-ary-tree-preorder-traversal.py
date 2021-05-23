"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.arr = []
        def preorder_trav(root):
            if root is None:
                return
            self.arr.append(root.val)
            for i in root.children:
                preorder_trav(i)

        preorder_trav(root)
        return self.arr