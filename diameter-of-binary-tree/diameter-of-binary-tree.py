# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self): 
        self.diameter = 0  
        
    def diameterOfBinaryTree(self, node: Optional[TreeNode]) -> int:
        
        
        def helper(root): 
        
            if not root:
                return 0 

            left_ans = helper(root.left) 

            right_ans = helper(root.right) 

            self.diameter = max(self.diameter, left_ans + right_ans) 
            return max(left_ans, right_ans) + 1 
        
        helper(node)
        
        return self.diameter
    
        
        
        
        
        
        