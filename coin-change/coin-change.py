from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        queue = deque([(amount,0)]) 
        
        seen = set([amount]) 
        while queue: 
            accumulated_amount, num_coins = queue.popleft()
            
            if accumulated_amount == 0: 
                return num_coins 
            
            for coin in coins: 
                if accumulated_amount - coin >= 0 and accumulated_amount - coin not in seen: 
                    queue.append((accumulated_amount-coin, num_coins+1)) 
                    seen.add(accumulated_amount - coin)
                    
        return -1
        