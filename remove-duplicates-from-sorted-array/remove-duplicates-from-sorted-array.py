class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        """
        2 pointers left and right
        
        1. Iterate the right pointer till the end of nums 
        2. if num at right pointer is not equal to num at left pointer -> increment left pointer and move the num@right to left 
        """
        
        left = 0 
        
        for right in range(len(nums)): 
            if nums[right] != nums[left]: 
                left += 1 
                nums[left] = nums[right] 
                
        return left + 1
        
        
        
 
                
        