# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_end_of_first_half(self, head): 
        
        #Initialize two pointers - p1 increments 1 step and p2 increments 2 steps at a time
        p1 = head 
        p2 = head 
        
        while p2.next is not None and p2.next.next is not None: 
            p1 = p1.next 
            p2 = p2.next.next
            
        return p1
    
    
    def reverse(self, head): 
        
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next 
            
            curr.next = prev 
            
            prev = curr 
            curr = next_node 
            
        return prev
        
    
        
        
    def isPalindrome(self, head: ListNode) -> bool:
        """
        1. Two pointers and find out the end of first-half and the end of list 
        2. Reverse the second-half in-place 
        3. Compare the two lists 
        4. reverse the second-half again to retain the original list 
        5. Return true or false 
        """
    
        
        if not head.next: 
            return True 
        
        
        

        

        p1_end = self.find_end_of_first_half(head)
                
        p2_reverse_head = self.reverse(p1_end.next)
        
        
        p1 = head
        p2 = p2_reverse_head 
        
    
        result = True 
        while result and p2: 
            if p1.val != p2.val: 
                result = False 
            
            p1 = p1.next 
            p2 = p2.next  
            
        
        p1_end.next = self.reverse(p2_reverse_head)
            
        return result 
        
        
        
        
        
            
 
            
        