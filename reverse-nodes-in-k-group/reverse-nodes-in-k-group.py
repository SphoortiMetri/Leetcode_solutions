# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,head,k): 
        prev = None 
        node = head 
        
        while k: 
            next_node = node.next 
            node.next = prev 
            
            prev = node 
            node = next_node 
            
            k -= 1 
        
        return prev
            
            
            
            
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0 
        
        ptr = head 
        
        while count < k and ptr: 
            ptr = ptr.next 
            count += 1 
         
        #if there are k nodes to reverse 
        if count == k: 
            
            #reverse first k nodes
            reverse_head = self.reverse(head,k)
            
            head.next = self.reverseKGroup(ptr,k)
            
            return reverse_head 
        
        return head 
            
            
            
            
        