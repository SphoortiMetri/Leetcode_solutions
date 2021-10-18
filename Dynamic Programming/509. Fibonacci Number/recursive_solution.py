class Solution:
    def fib(self, n: int) -> int: 
        memo = {} 
        def helper(n): 
            if n in memo: 
                return memo[n] 
            
            if n <2: 
                result = n 
                
            else: 
                result = helper(n-1) + helper(n-2) 
                
            memo[n] = result 
            return result
        return helper(n)
