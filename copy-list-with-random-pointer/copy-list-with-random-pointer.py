"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self): 
        self.visitedHash = {}
        
    def get_cloned_node(self, node):
        if node: 
            if node in self.visitedHash: 
                return self.visitedHash[node]

            new_node = Node(node.val, None, None) 
            self.visitedHash[node] = new_node
            return new_node
        else: 
            return None

        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None: 
            return None 
        
        old_node = head 
        new_node = Node(old_node.val, None, None)
        self.visitedHash[old_node] = new_node
        
        
        while old_node: 
            new_node.random = self.get_cloned_node(old_node.random) 
            new_node.next = self.get_cloned_node(old_node.next) 
            
            
            
            old_node = old_node.next 
            new_node = new_node.next
            
        return self.visitedHash[head]
            
        
   

        
        
        
        
        