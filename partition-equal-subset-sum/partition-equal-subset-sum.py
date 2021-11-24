class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums) 
        if sum_ % 2 != 0: 
            return False 
        
        def dfs(nums, curr_idx, subset_sum, cache):
            
            if cache[curr_idx][subset_sum] != -1: 
                return cache[curr_idx][subset_sum]
        
            if subset_sum == 0: 
                return True 

            if curr_idx == 0 or subset_sum < 0: 
                return False 

            result = dfs(nums, curr_idx-1, subset_sum - nums[curr_idx-1], cache)  or dfs(nums, curr_idx-1, subset_sum, cache)  
            cache[curr_idx][subset_sum] = result
            return result
        
        subset_sum = sum_//2
        n = len(nums)
        cache = [[-1 for i in range(sum_+1)]for j in range(n)]
        
        return dfs(nums, n-1, subset_sum, cache) 
        