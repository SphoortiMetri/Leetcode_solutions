class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Iterative solution 
        #create a dummy node to save the link to head 
        
        dummy = ListNode(-1) 
        
        dummy.next = head 
        prev_node = dummy 
        
        while head and head.next: 
            first_node = head 
            second_node = head.next 
            
            #swap 
            prev_node.next = second_node 
            first_node.next = second_node.next 
            second_node.next = first_node 
            
            #reset 
            prev_node = first_node 
            head = first_node.next
            
        return dummy.next
