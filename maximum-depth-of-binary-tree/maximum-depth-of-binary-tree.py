# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

DFS - Update max_depth once I reach a leaf node 
Base cases: 
Empty tree : return 0 


1 
 \
 2 
 
 depth: 1 
 Iterative solution: stack for DFS 

"""
class Solution:
    
    def __init__(self): 
        self.answer = 0 
    
   
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, depth):
            if root is None: 
                return
            if root.left is None and root.right is None: 
                self.answer = max(self.answer, depth) 
                
            helper(root.left, depth+1) 
            helper(root.right, depth + 1)
        
        if root is None: 
            return 0 
        
        helper(root, 1) 
        return self.answer
    
        
        
        
        
        
        

        
        
        
        
        