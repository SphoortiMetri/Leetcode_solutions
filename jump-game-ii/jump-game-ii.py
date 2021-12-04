class Solution:
    def jump(self, jumps: List[int]) -> int:
        
        n = len(jumps)
        
        def jump_recursive(i,memo):
            if i ==  n-1: 
                return 0 
            
            if jumps[i] == 0: 
                return math.inf
            
            if i in memo: 
                return memo[i]
            result = math.inf

            start, end = i+1, i + jumps[i] 
            while start < n and start <= end: 
                minJumps = jump_recursive(start,memo) 
                start += 1
                if minJumps != math.inf: 
                    result = min(result, minJumps+1) 
                    
            memo[i] = result 
            return memo[i]
        
        memo = {}
        return jump_recursive(0, memo)
                    
                
                
            
            
        
        
        
        
        
        