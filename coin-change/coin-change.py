from collections import deque
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        
        def count_change_recursive(denominations, total, currentIndex, memo):
        
            if total == 0:
                return 0

            n = len(denominations)
            if n == 0 or currentIndex >= n:
                return math.inf
            
            if memo[currentIndex][total] != -2: 
                return memo[currentIndex][total]

            count1 = math.inf

            if denominations[currentIndex] <= total:
                res = count_change_recursive(denominations, total - denominations[currentIndex], currentIndex, memo)
                if res != math.inf:
                    count1 = res + 1

            count2 = count_change_recursive(denominations, total, currentIndex + 1, memo)
            memo[currentIndex][total] = min(count1, count2)
            return memo[currentIndex][total]
        
        memo = [[-2 for i in range(amount+1)] for j in range(len(coins))]
        ans = count_change_recursive(coins, amount, 0, memo)
        if ans == math.inf: 
            return -1 
        else: 
            return ans

    

                    
                
                