class Solution:
    
    def __init__(self): 
        self.answer = 0 
    
   
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        stack = deque([(root,1)]) 
                
        while stack: 
            node, curr_depth = stack.pop() 
            self.answer = max (self.answer, curr_depth)
            if node.left: 
                stack.append((node.left, curr_depth+1))
            if node.right: 
                stack.append((node.right, curr_depth+1))
                
        return self.answer
