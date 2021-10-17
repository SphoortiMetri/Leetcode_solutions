class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None: 
            return head
        
        #first node 
        first_node = head 
        second_node = head.next 
        
        #swap nodes 
        first_node.next = self.swapPairs(head.next.next) 
        second_node.next = first_node 
        
        return second_node
