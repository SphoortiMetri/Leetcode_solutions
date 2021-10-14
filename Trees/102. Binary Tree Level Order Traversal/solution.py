# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = [] 
        if root is None:
                return None 

        queue = deque([root]) 
        
        while queue: 
                new_level = []
                for _ in range(len(queue)): 
                        node = queue.popleft() 
                        new_level.append(node.val) 
                        if node.left: 
                                queue.append(node.left) 
                        if node.right: 
                                queue.append(node.right) 

                levels.append(new_level)  

        return levels  
        
