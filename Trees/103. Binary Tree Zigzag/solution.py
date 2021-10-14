# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
            # WRITE YOUR BRILLIANT CODE HERE
        if root is None: 
            return []

        queue = deque([root])
        levels = []
        left_to_right = True
        while queue: 
            new_level = []
            for _ in range(len(queue)): 
                node = queue.popleft() 
                new_level.append(node.val)
                if node.left: 
                    queue.append(node.left) 

                if node.right: 
                    queue.append(node.right) 

            if not left_to_right: 
                new_level.reverse() 

            levels.append(new_level) 
            left_to_right = not left_to_right

        return levels
