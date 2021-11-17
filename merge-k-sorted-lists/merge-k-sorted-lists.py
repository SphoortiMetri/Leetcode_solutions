import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0: 
            return None 
        
        while len(lists) > 1: 
            merged = [] 
            
            for i in range(0,len(lists),2):
                list1 = lists[i] 
                if i+1 < len(lists):
                    list2 = lists[i+1] 
                else: 
                    list2 = None
                
                merged.append(self.merge2Lists(list1, list2)) 
                
            lists = merged 
        return lists[0] 
    
        
    def merge2Lists(self, l1,l2): 
        if not l1: 
            return l2
        
        if not l2: 
            return l1 
        
        dummy = curr = ListNode(-1) 
        
        while l1 and l2: 
            if l1.val < l2.val: 
                curr.next = ListNode(l1.val) 
                l1 = l1.next 
            else: 
                curr.next = ListNode(l2.val) 
                l2 = l2.next 
                
            curr = curr.next 
            
        if l1: 
            curr.next = l1
        if l2: 
            curr.next = l2
            
        return dummy.next
            
            
            
                
                
                
                
                
        
    
        

        