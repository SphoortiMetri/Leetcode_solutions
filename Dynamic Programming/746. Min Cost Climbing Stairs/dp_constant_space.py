class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        #the length of the dp array needs to be one more than the len of the cost since the top 
        #floor is the one above the last index 
        down_one = 0 
        down_two = 0 
        
        for i in range(2, len(costs)+1): 
            curr = min(costs[i-1]+down_one,costs[i-2]+down_two)
            down_two = down_one 
            down_one = curr
            
        return down_one
        
