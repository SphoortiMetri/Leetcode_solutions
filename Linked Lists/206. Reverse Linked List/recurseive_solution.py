# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1 -> 2 -> 3 -> 4 -> None 
        
        reverse(1), head = 1 -> 2->3 -> 4 -> None      p = 4 -> 3 -> 2 -> None; head.next(2); 2->1; 1 -> None; p is now 4 -> 3 -> 2 -> 1 -> None
        
        reverse(2), head = 2 -> 3 -> 4 -> None              p = 4 -> 3 -> None; head.next(3); 3 -> 2; 2 -> None; p is now 4 -> 3 -> 2 -> None 
        
        reverse(3), head = 3 -> 4 -> None                   p = 4 -> None; head.next(4); 4 -> 3; 3 -> None => p: 4 -> 3 -> None
        
        reverse(4), head = 4 -> None                        SInce, head.next is None -> returns 4 -> None
        
    
        """
        
        #base case 
        
        if head == None or head.next == None: 
            return head 
        
        p = self.reverselist(head.next) 
        #node's next value's next value is going to be node 
        head.next.next = head 
        
        #make sure that the last node's next value is None
        head.next = None
        
        return p
    
    
