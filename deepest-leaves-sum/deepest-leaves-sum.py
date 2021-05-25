# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.arr = []
        self.queue  = [root,None]
        level = 1
        while self.queue:
            pop = self.queue.pop(0)
            if pop is None:
                level += 1
                self.queue.append(None)
                if self.queue[0] is None:
                    break
                else:
                    continue
            if pop.left:
                self.queue.append(pop.left)
            if pop.right:
                self.queue.append(pop.right)
            if not pop.left and not pop.right:
                self.arr.append((pop,level))
        self.sum_ = 0
        # print(self.arr)
        for i,j in self.arr:
            print(i,j)
            if j == level-1:
            #     print('hi')
                self.sum_ += i.val
      
        return self.sum_
            
        
        
        
        
        
        
        
        