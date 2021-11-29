class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def rob_from(i):
            if i >= len(nums): 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            res = max(rob_from(i+1), nums[i] + rob_from(i+2)) 
            memo[i] = res
            return res
        
        return rob_from(0)
            
        