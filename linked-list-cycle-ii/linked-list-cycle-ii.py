# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def find_cycle_length(slow): 
            curr = slow 
            cycle_length = 0 
            while True: 
                curr = curr.next
                cycle_length += 1 
                if curr == slow: 
                    break 
                    
            return cycle_length 
                
        
        def find_start(head, cycle_length): 
            p1 = head 
            p2 = head
            
            while cycle_length != 0: 
                p2 = p2.next 
                cycle_length -= 1 
                
            while p1 != p2: 
                p1 = p1.next 
                p2 = p2.next 
                
            return p1             
            
        cycle_exists = False 
        slow = head 
        fast = head 
        
        while (fast is not None and fast.next is not None): 
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast: 
                cycle_exists = True 
                cycle_length = find_cycle_length(slow) 
                break 
                
        return find_start(head, cycle_length) if cycle_exists else None
        
        
                
        
        
        
        
        