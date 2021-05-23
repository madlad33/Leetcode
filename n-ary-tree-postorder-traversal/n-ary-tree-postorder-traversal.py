"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.arr = []
        
        def postorder_trav(root):
            if root is None:
                return
            for i in range(len(root.children)):
                postorder_trav(root.children[i])
            self.arr.append(root.val)
                
        postorder_trav(root)
        return self.arr
        