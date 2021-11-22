class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:\
        
        n = len(nums) 
        if n == 0: 
            return [-1,-1] 
        
        result = [] 
        
        def find_upper(nums,target): 
            left = 0 
            right = n - 1
            
            while left <= right: 
                mid = left + (right-left)// 2
                
                if nums[mid] == target: 
                    if mid == right or nums[mid+1] != target: 
                        return mid 
                    
                    left = mid + 1 
                    
                elif nums[mid] > target: 
                    right = mid - 1
                else: 
                    left = mid + 1
                    
            return -1 
        
        def find_lower(nums, target): 
            left = 0 
            right = n - 1
            
            while left <= right:
                mid = left + (right-left)// 2

                
                if nums[mid] == target: 
                    
                    if mid == left or nums[mid-1] != target: 
                        #found start 
                        return mid 
                    
                    #could be on the left 
                    right = mid - 1 
                    
                elif nums[mid] > target: 
                    right = mid -1 
                    
                else: 
                    left = mid + 1
                    
            return -1 
        
        lower_bound = find_lower(nums, target)
        upper_bound = find_upper(nums, target)
        
        return [lower_bound, upper_bound]
        
                    
    
        

        
    
            
        
            