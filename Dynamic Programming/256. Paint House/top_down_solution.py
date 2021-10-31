class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        RED = 0 
        BLUE = 1 
        GREEN = 2 
        
        def min_cost(costs, i, color): 
            
            if i == len(costs): 
                return 0 
            
            if cache[i][color] != -1: 
                return cache[i][color]
            
            if color == RED: 
                
                cost_blue = min_cost(costs, i+1, BLUE) 
                cost_green = min_cost(costs, i+1, GREEN) 
                res = costs[i][0] + min(cost_blue, cost_green) 
                cache[i][color] = res
                return res
                
            
            elif color == BLUE:  
                cost_red = min_cost(costs, i+1, RED) 
                cost_green = min_cost(costs, i+1, GREEN) 
                res = costs[i][1] + min(cost_red, cost_green) 
                cache[i][color] = res
                return res
                
        
            elif color == GREEN: 
                cost_red = min_cost(costs, i+1, RED) 
                cost_blue = min_cost(costs, i+1, BLUE) 
                res = costs[i][2] + min(cost_red, cost_blue) 
                cache[i][color] = res
                return res
            
            
        cache = [[-1 for i in range(3)] for j in range(len(costs))]
            
            
        start_with_red = min_cost(costs, 0, RED) 
        start_with_blue = min_cost(costs, 0, BLUE)
        start_with_green = min_cost(costs, 0, GREEN)
        
        return min(start_with_red,start_with_blue,start_with_green)
