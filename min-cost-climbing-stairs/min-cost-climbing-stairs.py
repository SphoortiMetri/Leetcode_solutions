class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(i): 
            if i <= 1: 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            down_one = cost[i-1] + climb(i-1)
            down_two = cost[i-2] + climb(i-2) 
            memo[i] = min(down_one, down_two)
            return memo[i]
        
        memo = {}
        n = len(cost)
        return climb(n)
                
            
            
        