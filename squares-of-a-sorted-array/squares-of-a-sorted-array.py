class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        result = [0] * n 
        
        left = 0 
        right = n-1
        highest_available = right
        
        while left <= right: 
            
            left_square = nums[left] ** 2 
            right_square = nums[right] ** 2 
            
            if left_square > right_square: 
                result[highest_available] = left_square 
                left += 1
                
            else: 
                result[highest_available] = right_square 
                right -= 1 
                
            highest_available -= 1 
            
        return result
                
            