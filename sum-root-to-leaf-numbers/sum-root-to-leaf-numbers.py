# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(curr, sum_): 
            if curr is None: 
                return 0 
            
            sum_ = sum_ * 10 + curr.val
            if curr.left is None and curr.right is None: 
                return sum_
            
            else: 
                return helper(curr.left, sum_)  + helper(curr.right, sum_) 
            
        return helper(root, 0)
        