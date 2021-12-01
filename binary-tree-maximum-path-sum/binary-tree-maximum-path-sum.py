import math 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def __init__(self):
        self.maximum_sum = -math.inf
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        
        def helper(root): 
            if root is None: 
                return 0
        
            left_sum = helper(root.left)
            right_sum = helper(root.right) 
            left_sum = max(left_sum, 0) 
            right_sum = max(right_sum, 0)
            curr_sum = left_sum + right_sum + root.val 
            self.maximum_sum  = max(self.maximum_sum , curr_sum) 
            return max(left_sum, right_sum) + root.val 
        
        helper(root)
        return self.maximum_sum
    
            
        