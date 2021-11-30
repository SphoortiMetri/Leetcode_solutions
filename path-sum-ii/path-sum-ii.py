# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper(curr_node, rem_sum, curr_path, result): 
            if curr_node == None: 
                return 
            
            curr_path.append(curr_node.val)
            
            if curr_node.val == rem_sum and curr_node.left is None and curr_node.right is None: 
                result.append(list(curr_path)) 
                
            else: 
                #left 
                if curr_node.left is not None: 
                    helper(curr_node.left, rem_sum-curr_node.val, curr_path, result) 
                if curr_node.right is not None: 
                    helper(curr_node.right, rem_sum-curr_node.val, curr_path, result) 
            del curr_path[-1]
            
        result = []
            
        helper(root, targetSum,[], result)
        return result
        