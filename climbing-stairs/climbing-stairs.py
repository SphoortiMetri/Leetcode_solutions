class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, memo): 
            
            if n == 0: 
                return 1 
            
            if n == 1: 
                return 1 

            if n == 2: 
                return 2 
            
            if n in memo: 
                return memo[n]

            res =  helper(n-1, memo) + helper(n-2, memo)
            memo[n] = res
            return memo[n]
        
        memo = {} 
        return helper(n,memo)