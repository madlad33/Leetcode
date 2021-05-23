# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level = 1
        queue = [root,None]
        val_sum,nodes = 0,0
        avg = []
        while queue:
            pop = queue.pop(0)
            if pop is None:
                avg.append(val_sum/nodes)
                queue.append(None)
                nodes = 0
                val_sum = 0
                if queue[0] is None:
                    break
                else:
                    continue
                level+=1
                
            val_sum += pop.val
            nodes += 1
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)
        return avg            
        