# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0

        queue = deque([root])
        depth = 0

        while queue: 
                depth += 1 
                for _ in range(len(queue)): 
                        node = queue.popleft() 

                        if node.left is None and node.right is None: 
                                return depth

                        if node.left: 
                                queue.append(node.left) 

                        if node.right: 
                                queue.append(node.right)
        return 0
        
