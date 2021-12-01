# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(curr, S, current_path): 
            if curr is None: 
                return 0 
            
            current_path.append(curr.val) 
            path_count = 0 
            path_sum = 0 
            
            for i in range(len(current_path)-1,-1,-1): 
                path_sum += current_path[i] 
                if path_sum == S: 
                    path_count += 1 
                    
            path_count += helper(curr.left, S, current_path) 
            path_count += helper(curr.right, S, current_path) 
            
            del current_path[-1] 
            return path_count
            
        return helper(root, targetSum, [])