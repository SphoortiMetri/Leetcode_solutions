# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return [] 
        
        right_most_nodes = [] 
        queue = deque([root])
        
        while queue: 
            new_level = []
            for i in range(len(queue)):
                node = queue.popleft() 
                new_level.append(node.val) 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
            
            right_most_nodes.append(new_level[-1])

        return right_most_nodes 
        
