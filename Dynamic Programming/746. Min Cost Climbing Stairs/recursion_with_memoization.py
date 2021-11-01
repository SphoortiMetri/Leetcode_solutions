class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def helper(i): 
            if i <= 1: 
                return 0
            
            if i in cache: 
                return cache[i] 
            
            
            down_one = cost[i-1] + helper(i-1)
            down_two =  cost[i-2] + helper(i-2) 
            
            res = min(down_one,down_two)
            cache[i] = res 
            return res
        
        cache = {}
        return helper(len(cost))
        
