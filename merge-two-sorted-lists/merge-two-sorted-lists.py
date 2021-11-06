# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None: 
            return l2 
 
        if l2 is None: 
            return l1
        
        l3 = dummy = ListNode(-1) 
        
        while l1 and l2: 
        
            if l1.val < l2.val: 
                l3.next = ListNode(l1.val) 
                l1 = l1.next 
                l3 = l3.next 
            else: 
                l3.next = ListNode(l2.val) 
                l2 = l2.next 
                l3 = l3.next 
                
        if l1: 
            l3.next = l1 
            
        if l2: 
            l3.next = l2 
            
        return dummy.next
            
            
        
        
            
        
        
            
        