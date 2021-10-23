class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0 
        p2 = 0 
        
        for p2 in range(len(nums)): 
            if nums[p2] != 0: 
                #swap elements at p1 and p2 
                temp = nums[p2] 
                nums[p2] = nums[p1] 
                nums[p1] = temp 
                
                p1 += 1 
                
        return p1+1
                
                
