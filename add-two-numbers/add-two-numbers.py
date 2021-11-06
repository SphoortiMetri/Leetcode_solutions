# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1 
        p2 = l2 
        p3 = dummy = ListNode(-1) 
        
        carry = 0 
        
        while p1 and p2: 
            sum_of_two = p1.val + p2.val + carry
            sum_ = sum_of_two % 10 
            
            p3.next = ListNode(sum_)
            carry = sum_of_two // 10 
            
            p1 = p1.next 
            p2 = p2.next 
            p3 = p3.next
            
        while p1: 
            sum_of_two = p1.val + carry 
            sum_ = sum_of_two % 10
            p3.next = ListNode(sum_)
            carry = sum_of_two // 10 
            
            p1 = p1.next 
            p3 = p3.next
            
        while p2: 
            sum_of_two = p2.val + carry 
            sum_ = sum_of_two % 10
            p3.next = ListNode(sum_)
            carry = sum_of_two // 10 
            
            p2 = p2.next 
            p3 = p3.next
            
        if carry > 0: 
            p3.next = ListNode(carry)
            
        return dummy.next
        