class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def two_sum(i, target_sum): 
            left = i + 1
            right = len(nums) -1 
            
            while left < right: 
                sum_ = nums[left] + nums[right] + nums[i]
                if sum_ == 0: 
                    res.append([nums[i], nums[left], nums[right]])
                    left+= 1 
                    right -= 1 
                    while left < right and nums[left] == nums[left-1]: 
                        left += 1
                elif sum_ > 0:
                    right -= 1  
                else: 
                    left += 1 
                    

            
            
        
        #sort the list to reduce complexity
        nums.sort()
        res = []
        
        for i in range(len(nums)): 
            if i == 0 or nums[i] != nums[i-1]: 
                two_sum(i,-nums[i]) 
        
        return res