class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        x1 = 1 
        n = len(nums) + 1
        for i in range(2,n): 
            x1 = x1 ^ i 
            
        x2 = nums[0] 
        for i in range(1,n-1): 
            x2 = x2 ^ nums[i]
            
        return x1 ^ x2
            
        
        