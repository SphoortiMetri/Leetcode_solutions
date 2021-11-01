class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        #the length of the dp array needs to be one more than the len of the cost since the top 
        #floor is the one above the last index 
        dp = [0 for i in range(len(costs)+1)] 
        
        for i in range(2, len(costs)+1): 
            dp[i] = min((costs[i-1]+dp[i-1]), (costs[i-2]+dp[i-2])) 
        
        return dp[-1]
