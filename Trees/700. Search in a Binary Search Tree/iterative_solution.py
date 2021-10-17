# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        if root is None: 
            return None 
        

        stack = deque([root])
        
        while stack: 
            node = stack.pop()
            if node.val == val: 
                return node 
            
            elif val < node.val and node.left is not None: 
                stack.append(node.left) 
            
            elif val > node.val and node.right is not None: 
                stack.append(node.right)
                
        return None
                
